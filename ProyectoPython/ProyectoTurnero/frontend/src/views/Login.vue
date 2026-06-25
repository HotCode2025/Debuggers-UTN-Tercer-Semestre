<!-- Inicio de sesión JWT y registro real de nuevos pacientes. -->
<template>
  <div class="min-h-screen bg-slate-100 flex flex-col justify-center items-center p-4 font-sans antialiased text-slate-800">
    <div class="bg-white p-8 rounded-xl shadow-md w-full max-w-md border border-slate-200">
      
      <div class="flex flex-col items-center mb-6">
        <img src="/src/assets/logo.png" alt="Mi Turnero" class="w-20 h-20 object-contain mb-2" />
        <h1 class="text-2xl font-bold tracking-tight text-slate-900">Mi Turnero</h1>
      </div>

      <div v-if="vistaActual === 'login'">
        <h2 class="text-lg font-bold text-slate-700 mb-4 text-center">Iniciar sesión</h2>
        
        <div v-if="mensajeLogin" class="bg-red-50 text-red-700 p-3 rounded-lg border border-red-200 text-xs font-semibold mb-4 text-center">
          {{ mensajeLogin }}
        </div>
        
        <form @submit.prevent="manejarLogin" class="space-y-4">
          <div>
            <label class="block text-xs font-bold uppercase text-slate-500 mb-1">
              Nombre de usuario
            </label>
            <input
              type="text"
              v-model="inputUsername"
              required
              autocomplete="username"
              placeholder="Ingrese su nombre de usuario"
              class="w-full border border-slate-300 p-2 rounded text-sm focus:border-teal-500 focus:ring-1 focus:ring-teal-500 outline-none"
            />
          </div>

          <div>
            <label class="block text-xs font-bold uppercase text-slate-500 mb-1">Contraseña</label>
            <input 
              type="password" 
              v-model="inputPassword"
              required 
              placeholder="Ingresar contraseña" 
              class="w-full border border-slate-300 p-2 rounded text-sm focus:border-teal-500 focus:ring-1 focus:ring-teal-500 outline-none" 
            />
          </div>

          <button
            type="submit"
            :disabled="ingresando"
            class="w-full bg-teal-600 hover:bg-teal-700 disabled:bg-slate-300 text-white font-semibold py-2 rounded transition-colors text-sm shadow-sm"
          >
            {{ ingresando ? 'Ingresando...' : 'Iniciar sesión' }}
          </button>
        </form>

        <div class="mt-4 flex flex-col items-center space-y-3 text-sm">
          <button @click="irARegistro" class="w-full border border-teal-600 text-teal-600 font-semibold py-2 rounded hover:bg-teal-50/50 transition-colors text-sm">
            Registrarse
          </button>
        </div>
      </div>

      <div v-else-if="vistaActual === 'registro'">
        <h2 class="text-lg font-bold text-slate-700 mb-4 text-center">Registro</h2>

        <div v-if="errorRegistro" class="bg-red-50 text-red-700 p-3 rounded-lg border border-red-200 text-xs font-semibold mb-4 text-center">
          {{ errorRegistro }}
        </div>
        
        <form @submit.prevent="manejarRegistro" class="space-y-3">
          <div class="grid grid-cols-2 gap-2">
            <div>
              <label class="block text-xs font-semibold text-slate-500 mb-0.5">Nombre</label>
              <input type="text" v-model="regNombre" required placeholder="Ej: Juan" class="w-full border border-slate-300 p-2 rounded text-sm outline-none focus:border-teal-500" />
            </div>
            <div>
              <label class="block text-xs font-semibold text-slate-500 mb-0.5">Apellido</label>
              <input type="text" v-model="regApellido" required placeholder="Ej: Pérez" class="w-full border border-slate-300 p-2 rounded text-sm outline-none focus:border-teal-500" />
            </div>
          </div>

          <div>
            <label class="block text-xs font-semibold text-slate-500 mb-0.5">Nombre de usuario</label>
            <input
              type="text"
              v-model="regUsername"
              required
              autocomplete="username"
              placeholder="Ej: juan.perez"
              class="w-full border border-slate-300 p-2 rounded text-sm outline-none focus:border-teal-500"
            />
          </div>

          <div>
            <label class="block text-xs font-semibold text-slate-500 mb-0.5">Documento</label>
            <div class="flex space-x-2">
              <select v-model="regTipoDoc" class="border border-slate-300 p-2 rounded bg-slate-50 text-sm outline-none">
                <option value="DNI">DNI</option>
                <option value="Pasaporte">Pasaporte</option>
              </select>
              <input type="text" v-model="regDni" required placeholder="Ingrese su número" class="w-full border border-slate-300 p-2 rounded text-sm outline-none focus:border-teal-500" />
            </div>
          </div>

          <div>
            <label class="block text-xs font-semibold text-slate-500 mb-1">Género</label>
            <div class="flex space-x-4 text-sm">
              <label class="flex items-center space-x-1.5 cursor-pointer">
                <input type="radio" v-model="regGenero" value="Femenino" class="accent-teal-600" required /> <span>Femenino</span>
              </label>
              <label class="flex items-center space-x-1.5 cursor-pointer">
                <input type="radio" v-model="regGenero" value="Masculino" class="accent-teal-600" /> <span>Masculino</span>
              </label>
              <label class="flex items-center space-x-1.5 cursor-pointer">
                <input type="radio" v-model="regGenero" value="Prefiero no decirlo" class="accent-teal-600" /> <span>Prefiero no decirlo</span>
              </label>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-2">
            <div>
              <label class="block text-xs font-semibold text-slate-500 mb-0.5">Provincia</label>
              <select v-model="regProvincia" @change="actualizarCiudadPorDefecto" class="w-full border border-slate-300 p-2 rounded text-sm bg-white outline-none focus:border-teal-500">
                <option v-for="(ciudades, prov) in mapaProvincias" :key="prov" :value="prov">
                  {{ prov }}
                </option>
              </select>
            </div>
            <div>
              <label class="block text-xs font-semibold text-slate-500 mb-0.5">Ciudad / Barrio</label>
              <select v-model="regCiudad" class="w-full border border-slate-300 p-2 rounded text-sm bg-white outline-none focus:border-teal-500">
                <option v-for="ciudad in ciudadesDisponibles" :key="ciudad" :value="ciudad">
                  {{ ciudad }}
                </option>
              </select>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-2">
            <div>
              <label class="block text-xs font-semibold text-slate-500 mb-0.5">Celular</label>
              <input type="text" v-model="regTelefono" required placeholder="11-1234-5678" class="w-full border border-slate-300 p-2 rounded text-sm outline-none focus:border-teal-500" />
            </div>
            <div>
              <label class="block text-xs font-semibold text-slate-500 mb-0.5">E-mail</label>
              <input type="email" v-model="regEmail" required placeholder="usuario@gmail.com" class="w-full border border-slate-300 p-2 rounded text-sm outline-none focus:border-teal-500" />
            </div>
          </div>

          <div>
            <label class="block text-xs font-semibold text-slate-500 mb-0.5">Contraseña</label>
            <input type="password" v-model="regPassword" required placeholder="Cree una contraseña" class="w-full border border-slate-300 p-2 rounded text-sm outline-none focus:border-teal-500" />
          </div>

          <button
            type="submit"
            :disabled="registrando"
            class="w-full bg-teal-600 hover:bg-teal-700 disabled:bg-slate-300 text-white font-bold py-2 rounded transition-colors text-sm mt-2 shadow-sm"
          >
            {{ registrando ? 'Registrando...' : 'Registrarse' }}
          </button>
        </form>
        <button @click="vistaActual = 'login'" class="w-full text-center text-sm text-slate-500 hover:underline mt-4 block">
          ← Volver al login
        </button>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useTurnosStore } from '../stores/turnos'
import api from "../services/api"

const router = useRouter()
const store = useTurnosStore()

// Estado compartido por las dos vistas del componente: acceso y registro.
const vistaActual = ref('login')
const mensajeLogin = ref(localStorage.getItem('mensajeSesion') || '')
const ingresando = ref(false)
const errorRegistro = ref('')
const registrando = ref(false)
// El mensaje de sesión vencida se consume una sola vez al volver al login.
localStorage.removeItem('mensajeSesion')

// Todos los perfiles se autentican mediante un nombre de usuario.
const inputUsername = ref('')
const inputPassword = ref('')

// Catálogo local usado para completar la radicación del nuevo paciente.
const mapaProvincias = {
  "Buenos Aires": ["Avellaneda", "Quilmes", "Mar del Plata", "Bahía Blanca", "La Plata", "Lanús"],
  "CABA": ["Palermo", "Belgrano", "Caballito", "Flores", "San Telmo", "Recoleta"],
  "Catamarca": ["San Fernando del Valle", "Andalgalá"],
  "Chaco": ["Resistencia", "Presidencia Roque Sáenz Peña"],
  "Chubut": ["Comodoro Rivadavia", "Puerto Madryn", "Trelew"],
  "Córdoba": ["Córdoba Capital", "Villa Carlos Paz", "Río Cuarto"],
  "Corrientes": ["Corrientes Capital", "Goya"],
  "Entre Ríos": ["Paraná", "Concordia", "Gualeguaychú"],
  "Formosa": ["Formosa Capital", "Clorinda"],
  "Jujuy": ["San Salvador de Jujuy", "San Pedro"],
  "La Pampa": ["Santa Rosa", "General Pico"],
  "La Rioja": ["La Rioja Capital", "Chilecito"],
  "Mendoza": ["Mendoza Capital", "San Rafael", "Godoy Cruz"],
  "Misiones": ["Posadas", "Puerto Iguazú", "Oberá"],
  "Neuquén": ["Neuquén Capital", "San Martín de los Andes"],
  "Río Negro": ["San Carlos de Bariloche", "Viedma", "Cipolletti"],
  "Salta": ["Salta Capital", "San Ramón de la Nueva Orán"],
  "San Juan": ["San Juan Capital", "Caucete"],
  "San Luis": ["San Luis Capital", "Villa Mercedes"],
  "Santa Cruz": ["Río Gallegos", "El Calafate"],
  "Santa Fe": ["Rosario", "Santa Fe Capital", "Rafaela"],
  "Santiago del Estero": ["Santiago del Estero Capital", "La Banda"],
  "Tierra del Fuego": ["Ushuaia", "Río Grande"],
  "Tucumán": ["San Miguel de Tucumán", "Yerba Buena"]
}

// Datos reactivos del formulario de alta que luego se envían a Django.
const regUsername = ref('')
const regNombre = ref('')
const regApellido = ref('')
const regTipoDoc = ref('DNI')
const regDni = ref('')
const regGenero = ref('Femenino')
const regProvincia = ref('Buenos Aires')
const regCiudad = ref('Avellaneda')
const regTelefono = ref('')
const regEmail = ref('')
const regPassword = ref('')

const ciudadesDisponibles = computed(() => {
  return mapaProvincias[regProvincia.value] || []
})

const actualizarCiudadPorDefecto = () => {
  if (ciudadesDisponibles.value.length > 0) {
    regCiudad.value = ciudadesDisponibles.value[0]
  }
}

const irARegistro = () => {
  mensajeLogin.value = ''
  errorRegistro.value = ''
  vistaActual.value = 'registro'
}

// Crea una cuenta real y deja el documento preparado para el primer ingreso.
const manejarRegistro = async () => {
  errorRegistro.value = ''
  registrando.value = true

  try {
    await api.post('auth/registro/', {
      username: regUsername.value,
      nombre: regNombre.value,
      apellido: regApellido.value,
      tipo_documento: regTipoDoc.value,
      documento: regDni.value,
      genero: regGenero.value,
      provincia: regProvincia.value,
      ciudad: regCiudad.value,
      telefono: regTelefono.value,
      email: regEmail.value,
      password: regPassword.value,
    })

    inputUsername.value = regUsername.value
    inputPassword.value = ''
    mensajeLogin.value = ''
    vistaActual.value = 'login'
    alert('Registro exitoso. Ya puedes iniciar sesión con tu usuario y contraseña.')
  } catch (error) {
    errorRegistro.value = obtenerMensajeRegistro(error.response?.data)
  } finally {
    registrando.value = false
  }
}

const obtenerMensajeRegistro = (datos) => {
  // DRF agrupa errores por campo; la interfaz presenta el primero para mantener
  // el formulario compacto y orientar la corrección inmediata.
  if (!datos) return 'No se pudo completar el registro.'

  const primerError = Object.values(datos).flat()[0]
  return typeof primerError === 'string' ? primerError : 'Revisa los datos ingresados.'
}

// Autentica con JWT, persiste la sesión y deriva a la pantalla del rol recibido.
const manejarLogin = async () => {
  mensajeLogin.value = ''
  ingresando.value = true

  try {
    const respuesta = await api.post('auth/login/', {
      username: inputUsername.value,
      password: inputPassword.value,
    })

    localStorage.setItem('access', respuesta.data.access)
    localStorage.setItem('refresh', respuesta.data.refresh)
    localStorage.setItem('usuario', JSON.stringify(respuesta.data.usuario))

    store.usuario = respuesta.data.usuario

    const rol = String(respuesta.data.usuario.rol || '').toUpperCase().trim()

    // Esta redirección inicial complementa los guardias globales del router.
    if (rol === 'MEDICO') {
      router.push('/medico')
    } else {
      router.push('/home')
    }
  } catch (error) {
    if (!error.response) {
      mensajeLogin.value = 'No se pudo conectar con el servidor. Verifica que Django este iniciado.'
    } else if (error.response.status === 401) {
      mensajeLogin.value = 'Usuario o contraseña incorrectos.'
    } else {
      mensajeLogin.value = error.response?.data?.detail || 'No se pudo iniciar sesión.'
    }
  } finally {
    ingresando.value = false
  }
}
</script>


