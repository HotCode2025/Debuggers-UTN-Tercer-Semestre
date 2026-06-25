// Cliente HTTP centralizado con autenticación JWT y renovación automática.
import axios from 'axios'

const baseURL = 'http://127.0.0.1:8000/api/'

const api = axios.create({
  baseURL,
})

// Limpieza única reutilizada cuando el refresh deja de ser válido.
const limpiarSesion = () => {
  localStorage.removeItem('access')
  localStorage.removeItem('refresh')
  localStorage.removeItem('usuario')
}

api.interceptors.request.use((config) => {
  // Todas las llamadas hechas con esta instancia reciben el access actual.
  const token = localStorage.getItem('access')

  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }

  return config
})

let renovandoToken = null

const renovarAccessToken = async () => {
  const refresh = localStorage.getItem('refresh')

  if (!refresh) {
    throw new Error('No hay refresh token.')
  }

  // Se usa axios sin interceptores para que la renovación no se intercepte a sí misma.
  const respuesta = await axios.post(`${baseURL}auth/refresh/`, { refresh })
  localStorage.setItem('access', respuesta.data.access)

  if (respuesta.data.refresh) {
    localStorage.setItem('refresh', respuesta.data.refresh)
  }

  return respuesta.data.access
}

api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const solicitudOriginal = error.config
    const esNoAutorizado = error.response?.status === 401
    const esRutaAutenticacion = solicitudOriginal?.url?.startsWith('auth/')

    // Solo se reintentan solicitudes comunes una vez; login y refresh deben
    // devolver su error original para evitar ciclos.
    if (!esNoAutorizado || !solicitudOriginal || solicitudOriginal._reintentada || esRutaAutenticacion) {
      return Promise.reject(error)
    }

    solicitudOriginal._reintentada = true

    try {
      // Varias respuestas 401 simultáneas comparten una sola renovación.
      if (!renovandoToken) {
        renovandoToken = renovarAccessToken().finally(() => {
          renovandoToken = null
        })
      }

      const nuevoAccess = await renovandoToken
      solicitudOriginal.headers = solicitudOriginal.headers || {}
      solicitudOriginal.headers.Authorization = `Bearer ${nuevoAccess}`

      return api(solicitudOriginal)
    } catch (refreshError) {
      // Si el refresh venció, se informa la causa al login y se abandona la sesión.
      limpiarSesion()
      localStorage.setItem('mensajeSesion', 'Tu sesión venció. Inicia sesión nuevamente.')

      if (window.location.pathname !== '/') {
        window.location.replace('/')
      }

      return Promise.reject(refreshError)
    }
  },
)

export default api
