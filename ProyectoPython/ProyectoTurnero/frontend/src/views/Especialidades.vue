<!-- Segundo paso de la reserva: especialidades disponibles en el centro elegido. -->
<template>
  <div class="min-h-screen bg-slate-100 font-sans antialiased flex flex-col">
    <header class="bg-white border-b border-slate-200 px-6 py-4 shadow-sm flex items-center justify-between">
      <div class="flex items-center space-x-3">
        <img src="/src/assets/logo.png" alt="Mi Turnero" class="w-12 h-12 object-contain" />
        <div>
          <h1 class="text-xl font-bold tracking-tight text-slate-900">Mi Turnero</h1>
          <span class="text-xs text-slate-500">Seleccion de especialidad</span>
        </div>
      </div>
      <button @click="router.push('/centros')" class="text-sm font-semibold text-teal-600 hover:underline">
        Volver
      </button>
    </header>

    <main class="flex-grow max-w-md w-full mx-auto p-6 flex flex-col justify-center">
      <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
        <h2 class="text-lg font-bold text-slate-800 mb-2">Que especialidad requiere?</h2>
        <p class="text-xs text-slate-400 mb-4">
          {{ establecimientoNombre }}
        </p>

        <p v-if="error" class="bg-red-50 text-red-700 p-3 rounded-lg border border-red-200 text-xs font-semibold mb-4">
          {{ error }}
        </p>

        <form @submit.prevent="avanzarAProfesionales" class="space-y-4">
          <div>
            <label class="block text-xs font-bold uppercase text-slate-500 mb-1">
              Especialidades disponibles
            </label>
            <select
              v-model.number="especialidadId"
              required
              class="w-full border border-slate-300 p-2.5 rounded text-sm bg-slate-50 outline-none focus:border-teal-500 focus:ring-1 focus:ring-teal-500 text-slate-700 block"
            >
              <option value="" disabled>Elija una especialidad</option>
              <option v-for="esp in especialidades" :key="esp.id" :value="esp.id">
                {{ esp.nombre }}
              </option>
            </select>
          </div>

          <button
            type="submit"
            class="w-full bg-teal-600 hover:bg-teal-700 text-white font-semibold py-2.5 rounded transition-colors text-sm shadow-sm"
          >
            Continuar a profesionales
          </button>
        </form>
      </div>
    </main>
  </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useTurnosStore } from '../stores/turnos'
import api from '../services/api'

const router = useRouter()
const store = useTurnosStore()

// Opciones ofrecidas por el establecimiento elegido y selección del formulario.
const especialidades = ref([])
const especialidadId = ref('')
const error = ref('')

const establecimientoNombre = computed(() => {
  return store.turnoProceso.establecimiento?.nombre || 'Primero debe seleccionar un establecimiento.'
})

onMounted(async () => {
  // El acceso directo por URL se redirige porque falta el contexto del centro.
  const establecimiento = store.turnoProceso.establecimiento

  if (!establecimiento?.id) {
    router.push('/centros')
    return
  }

  try {
    const respuesta = await api.get('especialidades/', {
      params: {
        establecimiento_id: establecimiento.id,
      },
    })

    especialidades.value = respuesta.data
  } catch (err) {
    error.value = 'No se pudieron cargar las especialidades.'
  }
})

const avanzarAProfesionales = () => {
  const especialidad = especialidades.value.find((esp) => esp.id === especialidadId.value)

  if (!especialidad) {
    error.value = 'Seleccione una especialidad valida.'
    return
  }

  // Una nueva especialidad invalida médico, fecha y hora del intento anterior.
  store.turnoProceso.especialidad = especialidad
  store.turnoProceso.profesional = null
  store.turnoProceso.fecha = ''
  store.turnoProceso.hora = ''
  router.push('/profesionales')
}
</script>
