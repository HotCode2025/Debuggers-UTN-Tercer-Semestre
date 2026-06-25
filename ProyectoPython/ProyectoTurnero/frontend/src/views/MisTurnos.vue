<!-- Historial real del paciente con filtro de activos y cancelación. -->
<template>
  <div class="min-h-screen bg-slate-100 font-sans text-slate-800">
    <Navbar />

    <main class="max-w-4xl mx-auto px-4 py-8">
      <div class="flex flex-col sm:flex-row sm:items-end sm:justify-between gap-4 mb-6">
        <div>
          <h1 class="text-2xl font-bold text-slate-900">Mis turnos</h1>
          <p class="text-sm text-slate-500 mt-1">Consulta tus turnos y cancela los que ya no necesites.</p>
        </div>

        <div class="inline-flex bg-white border border-slate-200 rounded p-1 self-start">
          <button
            type="button"
            @click="cargarTurnos"
            :class="filtro === 'todos' ? 'bg-teal-600 text-white' : 'text-slate-600 hover:bg-slate-100'"
            class="px-4 py-2 rounded text-sm font-semibold"
          >
            Todos
          </button>
          <button
            type="button"
            @click="cargarActivos"
            :class="filtro === 'activos' ? 'bg-teal-600 text-white' : 'text-slate-600 hover:bg-slate-100'"
            class="px-4 py-2 rounded text-sm font-semibold"
          >
            Activos
          </button>
        </div>
      </div>

      <p v-if="error" class="bg-red-50 text-red-700 border border-red-200 rounded p-3 text-sm mb-4">
        {{ error }}
      </p>

      <p v-if="mensaje" class="bg-emerald-50 text-emerald-700 border border-emerald-200 rounded p-3 text-sm mb-4">
        {{ mensaje }}
      </p>

      <div v-if="cargando" class="bg-white border border-slate-200 rounded p-6 text-sm text-slate-500">
        Cargando turnos...
      </div>

      <div v-else-if="turnos.length" class="space-y-3">
        <article
          v-for="turno in turnos"
          :key="turno.id"
          class="bg-white border border-slate-200 rounded shadow-sm p-5"
        >
          <div class="flex flex-col md:flex-row md:items-start md:justify-between gap-4">
            <div class="min-w-0">
              <div class="flex flex-wrap items-center gap-2 mb-2">
                <h2 class="font-bold text-lg text-slate-900">
                  {{ turno.especialidad?.nombre || 'Especialidad' }}
                </h2>
                <span :class="claseEstado(turno.estado)" class="px-2 py-1 rounded text-xs font-bold">
                  {{ textoEstado(turno.estado) }}
                </span>
              </div>

              <p class="font-semibold text-slate-700">
                {{ nombreProfesional(turno.profesional) }}
              </p>
              <p class="text-sm text-slate-500 mt-1">
                {{ turno.establecimiento?.nombre || 'Establecimiento' }}
              </p>
              <p v-if="turno.establecimiento?.direccion" class="text-sm text-slate-500">
                {{ turno.establecimiento.direccion }}
              </p>

              <div class="flex flex-wrap gap-x-6 gap-y-1 mt-3 text-sm">
                <p><span class="font-semibold">Fecha:</span> {{ formatearFecha(turno.fecha) }}</p>
                <p><span class="font-semibold">Hora:</span> {{ formatearHora(turno.hora) }}</p>
              </div>
            </div>

            <button
              v-if="turno.estado === 'RESERVADO'"
              type="button"
              @click="cancelarTurno(turno)"
              :disabled="cancelandoId === turno.id"
              class="bg-red-600 hover:bg-red-700 disabled:bg-slate-300 text-white px-4 py-2 rounded text-sm font-semibold shrink-0"
            >
              {{ cancelandoId === turno.id ? 'Cancelando...' : 'Cancelar turno' }}
            </button>
          </div>
        </article>
      </div>

      <div v-else class="bg-white border border-slate-200 rounded p-8 text-center">
        <h2 class="font-bold text-slate-800">No hay turnos para mostrar</h2>
        <p class="text-sm text-slate-500 mt-1">
          {{ filtro === 'activos' ? 'No tienes turnos reservados.' : 'Cuando reserves un turno aparecera aqui.' }}
        </p>
        <button
          type="button"
          @click="router.push('/centros')"
          class="mt-4 bg-teal-600 hover:bg-teal-700 text-white px-5 py-2.5 rounded text-sm font-semibold"
        >
          Sacar un turno
        </button>
      </div>
    </main>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import Navbar from '../components/Navbar.vue'
import api from '../services/api'

const router = useRouter()

// Listado visible, filtro activo y estados de las solicitudes del paciente.
const turnos = ref([])
const filtro = ref('todos')
const cargando = ref(false)
const cancelandoId = ref(null)
const error = ref('')
const mensaje = ref('')

onMounted(cargarTurnos)

// Función común para las pestañas Todos y Activos. El endpoint cambia, pero el
// manejo de carga, errores y reemplazo del listado permanece igual.
const obtenerTurnos = async (endpoint, nuevoFiltro) => {
  cargando.value = true
  error.value = ''
  mensaje.value = ''
  filtro.value = nuevoFiltro

  try {
    const respuesta = await api.get(endpoint)
    turnos.value = respuesta.data
  } catch (err) {
    turnos.value = []
    error.value = err.response?.data?.error || 'No se pudieron cargar tus turnos.'
  } finally {
    cargando.value = false
  }
}

function cargarTurnos() {
  return obtenerTurnos('mis-turnos/', 'todos')
}

function cargarActivos() {
  return obtenerTurnos('mis-turnos/activos/', 'activos')
}

const cancelarTurno = async (turno) => {
  // La confirmación ocurre antes de modificar estados o llamar al backend.
  const confirmado = window.confirm(
    `¿Confirmas que deseas cancelar el turno del ${formatearFecha(turno.fecha)} a las ${formatearHora(turno.hora)}?`,
  )

  if (!confirmado) return

  error.value = ''
  mensaje.value = ''
  cancelandoId.value = turno.id

  try {
    await api.post(`turnos/${turno.id}/cancelar/`)
    await (filtro.value === 'activos' ? cargarActivos() : cargarTurnos())
    mensaje.value = 'El turno fue cancelado correctamente.'
  } catch (err) {
    error.value = err.response?.data?.error || 'No se pudo cancelar el turno.'
  } finally {
    cancelandoId.value = null
  }
}

const nombreProfesional = (profesional) => {
  if (!profesional) return 'Profesional'
  return `${profesional.nombre || ''} ${profesional.apellido || ''}`.trim() || 'Profesional'
}

// La fecha se interpreta como UTC para evitar que el huso horario del navegador
// la desplace al día anterior.
const formatearFecha = (fecha) => {
  if (!fecha) return ''
  return new Intl.DateTimeFormat('es-AR', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    timeZone: 'UTC',
  }).format(new Date(`${fecha}T00:00:00Z`))
}

const formatearHora = (hora) => hora?.slice(0, 5) || ''

const textoEstado = (estado) => {
  // Se separa el valor técnico almacenado en Django del texto mostrado.
  const estados = {
    RESERVADO: 'Reservado',
    CANCELADO: 'Cancelado',
    ATENDIDO: 'Atendido',
  }
  return estados[estado] || estado
}

const claseEstado = (estado) => {
  const clases = {
    RESERVADO: 'bg-teal-50 text-teal-700',
    CANCELADO: 'bg-red-50 text-red-700',
    ATENDIDO: 'bg-emerald-50 text-emerald-700',
  }
  return clases[estado] || 'bg-slate-100 text-slate-600'
}
</script>
