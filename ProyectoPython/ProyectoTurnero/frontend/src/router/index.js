// Define las pantallas y protege la navegación según autenticación y rol.
import { createRouter, createWebHistory } from 'vue-router'

import Login from '../views/Login.vue'
import Home from '../views/Home.vue'
import Centros from '../views/Centros.vue'
import Especialidades from '../views/Especialidades.vue'
import Profesionales from '../views/Profesionales.vue'
import Confirmar from '../views/Confirmar.vue'
import MisTurnos from '../views/MisTurnos.vue'
import MedicoHome from '../views/MedicoHome.vue'

// Cada meta define si la ruta requiere sesión y qué rol puede verla.
const routes = [
  { path: '/', name: 'Login', component: Login, meta: { soloInvitados: true } },
  { path: '/home', name: 'Home', component: Home, meta: { requiereAuth: true, rol: 'PACIENTE' } },
  { path: '/centros', name: 'Centros', component: Centros, meta: { requiereAuth: true, rol: 'PACIENTE' } },
  { path: '/especialidades', name: 'Especialidades', component: Especialidades, meta: { requiereAuth: true, rol: 'PACIENTE' } },
  { path: '/profesionales', name: 'Profesionales', component: Profesionales, meta: { requiereAuth: true, rol: 'PACIENTE' } },
  { path: '/confirmar', name: 'Confirmar', component: Confirmar, meta: { requiereAuth: true, rol: 'PACIENTE' } },
  { path: '/mis-turnos', name: 'MisTurnos', component: MisTurnos, meta: { requiereAuth: true, rol: 'PACIENTE' } },
  { path: '/medico', name: 'MedicoHome', component: MedicoHome, meta: { requiereAuth: true, rol: 'MEDICO' } },
  { path: '/:pathMatch(.*)*', redirect: '/' },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

const obtenerRolGuardado = () => {
  // El parseo defensivo evita que un valor corrupto en localStorage rompa Vue.
  try {
    const usuario = JSON.parse(localStorage.getItem('usuario'))
    return String(usuario?.rol || '').toUpperCase().trim()
  } catch {
    localStorage.removeItem('usuario')
    return ''
  }
}

router.beforeEach((to) => {
  // El guardia usa los datos persistidos para funcionar también al recargar.
  const token = localStorage.getItem('access')
  const rol = obtenerRolGuardado()
  const rolValido = rol === 'PACIENTE' || rol === 'MEDICO'

  // Un token sin perfil compatible se considera una sesión incompleta y se limpia.
  if (token && !rolValido) {
    localStorage.removeItem('access')
    localStorage.removeItem('refresh')
    localStorage.removeItem('usuario')
    return { name: 'Login' }
  }

  if (to.meta.requiereAuth && (!token || !rolValido)) {
    return { name: 'Login' }
  }

  if (to.meta.soloInvitados && token && rolValido) {
    return rol === 'MEDICO' ? { name: 'MedicoHome' } : { name: 'Home' }
  }

  // Los intentos de cruzar perfiles vuelven al inicio autorizado del usuario.
  if (to.meta.rol && rol !== to.meta.rol) {
    if (rol === 'MEDICO') return { name: 'MedicoHome' }
    if (rol === 'PACIENTE') return { name: 'Home' }
    return { name: 'Login' }
  }

  return true
})

export default router
