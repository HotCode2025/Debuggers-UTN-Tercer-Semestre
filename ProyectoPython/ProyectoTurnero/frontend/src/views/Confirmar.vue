<!-- Paso final: consulta horarios reales y envía la reserva al backend. -->
<template>
  <div class="min-h-screen bg-slate-100 font-sans antialiased flex flex-col items-center justify-center p-4">
    <div v-if="errorDeFlujo" class="bg-white w-full max-w-md rounded-2xl shadow-md border border-red-200 overflow-hidden text-center p-6 space-y-4">
      <h2 class="text-xl font-bold text-slate-800">Faltan datos del turno</h2>
      <p class="text-sm text-slate-600">
        Debe seleccionar establecimiento, especialidad y profesional antes de confirmar.
      </p>
      <button @click="router.push('/centros')" class="w-full bg-red-600 hover:bg-red-700 text-white font-semibold py-2 rounded text-sm transition-colors shadow-sm">
        Volver a centros
      </button>
    </div>

    <div v-else class="bg-white w-full max-w-md rounded-2xl shadow-md border border-slate-200 overflow-hidden">
      <div class="bg-slate-900 text-white p-6 text-center relative">
        <div class="flex justify-center mb-2">
          <img src="/src/assets/logo.png" alt="Logo Mi Turnero" class="w-16 h-16 object-contain" />
        </div>
        <h2 class="text-xl font-bold tracking-tight">Resumen de su turno</h2>
        <p class="text-xs text-slate-400 mt-1">Seleccione fecha y horario disponible</p>
      </div>

      <form @submit.prevent="confirmarYFinalizar" class="p-6 space-y-4 text-sm">
        <p v-if="mensajeError" class="bg-red-50 text-red-700 p-3 rounded-lg border border-red-200 text-xs font-semibold">
          {{ mensajeError }}
        </p>

        <div>
          <h3 class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-1.5">Datos del paciente</h3>
          <div class="bg-slate-50 p-3 rounded-lg border border-slate-200 space-y-1">
            <p class="text-slate-800"><span class="font-semibold text-slate-500">Nombre:</span> {{ store.usuario.nombre || 'Usuario logueado' }}</p>
            <p class="text-slate-800"><span class="font-semibold text-slate-500">Rol:</span> {{ store.usuario.rol || 'Paciente' }}</p>
          </div>
        </div>

        <div>
          <h3 class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-1.5">Detalles de la cita</h3>
          <div class="bg-teal-50/50 p-3 rounded-lg border border-teal-100 space-y-1">
            <p class="text-slate-800"><span class="font-semibold text-teal-700">Centro:</span> {{ store.turnoProceso.establecimiento?.nombre }}</p>
            <p class="text-slate-800"><span class="font-semibold text-teal-700">Especialidad:</span> {{ store.turnoProceso.especialidad?.nombre }}</p>
            <p class="text-slate-800"><span class="font-semibold text-teal-700">Profesional:</span> {{ store.turnoProceso.profesional?.nombre }}</p>
          </div>
        </div>

        <div>
          <h3 class="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">Asignacion de turno</h3>
          <div class="space-y-3">
            <div>
              <label class="block text-xs font-semibold text-slate-500 mb-1">Elegir fecha</label>
              <input
                type="date"
                v-model="inputFecha"
                required
                @change="cargarHorarios"
                class="w-full border border-slate-300 p-2 rounded text-sm bg-slate-50 outline-none focus:border-teal-500 text-slate-700"
              />
            </div>

            <div>
              <label class="block text-xs font-semibold text-slate-500 mb-1">Elegir horario</label>
              <select
                v-model="inputHora"
                required
                :disabled="!horarios.length"
                class="w-full border border-slate-300 p-2 rounded text-sm bg-slate-50 outline-none focus:border-teal-500 text-slate-700"
              >
                <option value="" disabled>Seleccione un horario</option>
                <option v-for="hora in horarios" :key="hora" :value="hora">
                  {{ hora }}
                </option>
              </select>
              <p v-if="inputFecha && !horarios.length && !mensajeError" class="text-xs text-slate-500 mt-2">
                No hay horarios disponibles para esa fecha.
              </p>
            </div>
          </div>
        </div>

        <div class="pt-2">
          <button
            type="submit"
            :disabled="guardando"
            class="w-full bg-teal-600 hover:bg-teal-700 disabled:bg-slate-400 text-white font-bold py-2.5 rounded text-sm transition-colors shadow-sm text-center block"
          >
            {{ guardando ? 'Guardando...' : 'Confirmar y guardar turno' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useTurnosStore } from '../stores/turnos'
import api from '../services/api'

const router = useRouter()
const store = useTurnosStore()

// Datos temporales de la reserva y estados de interacción con la API.
const inputFecha = ref(store.turnoProceso.fecha || '')
const inputHora = ref(store.turnoProceso.hora || '')
const horarios = ref([])
const mensajeError = ref('')
const guardando = ref(false)

const errorDeFlujo = computed(() => {
  // Evita solicitudes incompletas si se accede directamente a esta ruta.
  return !store.turnoProceso.establecimiento?.id ||
    !store.turnoProceso.especialidad?.id ||
    !store.turnoProceso.profesional?.id
})

const cargarHorarios = async () => {
  // Cambiar la fecha invalida la hora previamente seleccionada.
  mensajeError.value = ''
  inputHora.value = ''
  horarios.value = []

  if (errorDeFlujo.value || !inputFecha.value) return

  try {
    const respuesta = await api.get('horarios-disponibles/', {
      params: {
        profesional_id: store.turnoProceso.profesional.id,
        establecimiento_id: store.turnoProceso.establecimiento.id,
        especialidad_id: store.turnoProceso.especialidad.id,
        fecha: inputFecha.value,
      },
    })

    horarios.value = respuesta.data
  } catch (err) {
    mensajeError.value = 'No se pudieron cargar los horarios disponibles.'
  }
}

const confirmarYFinalizar = async () => {
  if (errorDeFlujo.value || !inputFecha.value || !inputHora.value) return

  guardando.value = true
  mensajeError.value = ''

  try {
    // Django identifica al paciente por JWT; el cuerpo solo describe la cita.
    await api.post('turnos/reservar/', {
      profesional_id: store.turnoProceso.profesional.id,
      establecimiento_id: store.turnoProceso.establecimiento.id,
      especialidad_id: store.turnoProceso.especialidad.id,
      fecha: inputFecha.value,
      hora: inputHora.value,
    })

    // Pinia conserva un resumen local para mantener coherencia al navegar.
    store.turnoProceso.fecha = inputFecha.value
    store.turnoProceso.hora = inputHora.value
    store.confirmarTurnoActual()

    alert('Turno guardado con exito.')
    router.push('/home')
  } catch (err) {
    mensajeError.value = err.response?.data?.error || 'No se pudo reservar el turno.'
  } finally {
    guardando.value = false
  }
}
</script>
