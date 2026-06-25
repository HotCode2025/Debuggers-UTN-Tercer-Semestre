<!-- Panel médico para agenda, estados de turnos y CRUD de disponibilidades. -->
<template>
  <div class="min-h-screen bg-slate-100 font-sans antialiased text-slate-800 flex flex-col">
    <header class="bg-white border-b border-slate-200 px-6 py-4 shadow-sm flex items-center justify-between">
      <div class="flex items-center space-x-3">
        <img src="/src/assets/logo.png" alt="Mi Turnero" class="w-12 h-12 object-contain" />
        <div>
          <h1 class="text-xl font-bold tracking-tight text-slate-900 leading-none">Panel medico</h1>
          <span class="text-xs text-slate-500">Gestion de agenda y turnos</span>
        </div>
      </div>
      <div class="text-right text-sm">
        <p class="font-medium text-slate-700">Hola, {{ store.usuario.username || store.usuario.nombre || 'Profesional' }}</p>
        <button @click="cerrarSesion" class="text-xs text-red-600 hover:underline font-semibold mt-0.5 block ml-auto">
          Cerrar sesion
        </button>
      </div>
    </header>

    <main class="flex-grow max-w-5xl w-full mx-auto p-6">
      <div class="mb-6">
        <h2 class="text-2xl font-bold text-slate-800 mb-2">Agenda del profesional</h2>
        <p class="text-slate-500 text-sm">
          Desde aca podes revisar turnos, marcar atenciones, cancelar turnos y administrar disponibilidades.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
        <button @click="cargarTurnos" class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm hover:border-teal-500 text-left">
          <h3 class="font-bold text-slate-800">Mis turnos</h3>
          <p class="text-xs text-slate-400 mt-1">Toda la agenda.</p>
        </button>

        <button @click="cargarTurnosActivos" class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm hover:border-teal-500 text-left">
          <h3 class="font-bold text-slate-800">Activos</h3>
          <p class="text-xs text-slate-400 mt-1">Solo reservados.</p>
        </button>

        <button @click="cargarDisponibilidades" class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm hover:border-teal-500 text-left">
          <h3 class="font-bold text-slate-800">Disponibilidad</h3>
          <p class="text-xs text-slate-400 mt-1">Horarios cargados.</p>
        </button>

        <button @click="abrirFormularioNuevo" class="bg-teal-600 p-5 rounded-xl border border-teal-700 shadow-sm hover:bg-teal-700 text-left text-white">
          <h3 class="font-bold">Nueva disponibilidad</h3>
          <p class="text-xs text-teal-100 mt-1">Crear horario.</p>
        </button>
      </div>

      <section class="bg-white rounded-xl border border-slate-200 shadow-sm p-5 mb-6">
        <h3 class="font-bold text-slate-800 mb-3">Buscar agenda por fecha</h3>
        <form @submit.prevent="cargarAgendaPorFecha" class="flex flex-col sm:flex-row gap-3">
          <input
            type="date"
            v-model="fechaAgenda"
            required
            class="border border-slate-300 p-2.5 rounded text-sm bg-slate-50 outline-none focus:border-teal-500"
          />
          <button type="submit" class="bg-slate-800 hover:bg-slate-900 text-white font-semibold px-5 py-2.5 rounded text-sm">
            Buscar
          </button>
        </form>
      </section>

      <section v-if="mostrarFormulario" class="bg-white rounded-xl border border-slate-200 shadow-sm p-5 mb-6">
        <div class="flex items-center justify-between gap-3 mb-3">
          <h3 class="font-bold text-slate-800">
            {{ disponibilidadEditandoId ? 'Editar disponibilidad' : 'Crear disponibilidad' }}
          </h3>
          <button
            v-if="disponibilidadEditandoId"
            type="button"
            @click="cancelarEdicion"
            class="text-sm font-semibold text-slate-500 hover:text-slate-800"
          >
            Cancelar edicion
          </button>
        </div>
        <form @submit.prevent="guardarDisponibilidad" class="grid grid-cols-1 md:grid-cols-3 gap-3">
          <select v-model="ciudadSeleccionada" @change="cargarEstablecimientos" required class="border border-slate-300 p-2.5 rounded text-sm bg-white">
            <option value="" disabled>Ciudad</option>
            <option v-for="ciudad in ciudades" :key="ciudad.id" :value="ciudad.id">
              {{ ciudad.nombre }}, {{ ciudad.provincia }}
            </option>
          </select>

          <select v-model="form.establecimiento_id" @change="cargarEspecialidades" required class="border border-slate-300 p-2.5 rounded text-sm bg-white">
            <option value="" disabled>Establecimiento</option>
            <option v-for="establecimiento in establecimientos" :key="establecimiento.id" :value="establecimiento.id">
              {{ establecimiento.nombre }}
            </option>
          </select>

          <select v-model="form.especialidad_id" required class="border border-slate-300 p-2.5 rounded text-sm bg-white">
            <option value="" disabled>Especialidad</option>
            <option v-for="especialidad in especialidades" :key="especialidad.id" :value="especialidad.id">
              {{ especialidad.nombre }}
            </option>
          </select>

          <select v-model="form.dia_semana" required class="border border-slate-300 p-2.5 rounded text-sm bg-white">
            <option value="" disabled>Dia de semana</option>
            <option value="0">Lunes</option>
            <option value="1">Martes</option>
            <option value="2">Miercoles</option>
            <option value="3">Jueves</option>
            <option value="4">Viernes</option>
          </select>
          <input v-model="form.hora_inicio" type="time" required class="border border-slate-300 p-2.5 rounded text-sm" />
          <input v-model="form.hora_fin" type="time" required class="border border-slate-300 p-2.5 rounded text-sm" />
          <input v-model="form.duracion_turno_minutos" type="number" min="1" required placeholder="Duracion en minutos" class="border border-slate-300 p-2.5 rounded text-sm" />
          <button type="submit" class="md:col-span-3 bg-teal-600 hover:bg-teal-700 text-white font-semibold py-2.5 rounded text-sm">
            {{ disponibilidadEditandoId ? 'Guardar cambios' : 'Guardar disponibilidad' }}
          </button>
        </form>
      </section>

      <p v-if="error" class="bg-red-50 text-red-700 p-3 rounded-lg border border-red-200 text-xs font-semibold mb-4">
        {{ error }}
      </p>

      <p v-if="mensaje" class="bg-emerald-50 text-emerald-700 p-3 rounded-lg border border-emerald-200 text-xs font-semibold mb-4">
        {{ mensaje }}
      </p>

      <section class="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
        <div class="px-5 py-4 border-b border-slate-100 flex items-center justify-between">
          <h3 class="font-bold text-slate-800">{{ tituloListado }}</h3>
          <span class="text-xs text-slate-400">{{ items.length }} registro/s</span>
        </div>

        <div v-if="items.length" class="divide-y divide-slate-100">
          <article v-for="item in items" :key="item.id" class="p-5 text-sm">
            <div class="flex flex-col md:flex-row md:items-start md:justify-between gap-3">
              <div>
                <p class="font-bold text-slate-900">{{ tituloItem(item) }}</p>
                <p class="text-slate-500 mt-1">{{ detalleItem(item) }}</p>
                <p v-if="modo === 'turnos' && detallePaciente(item.usuario)" class="text-xs text-slate-500 mt-1">
                  {{ detallePaciente(item.usuario) }}
                </p>
                <p v-if="item.estado" class="text-xs text-teal-700 font-semibold mt-2">Estado: {{ item.estado }}</p>
              </div>

              <div v-if="modo === 'turnos'" class="flex gap-2">
                <button
                  @click="marcarAtendido(item)"
                  :disabled="item.estado !== 'RESERVADO'"
                  class="bg-emerald-600 hover:bg-emerald-700 disabled:bg-slate-300 text-white font-semibold px-3 py-2 rounded text-xs"
                >
                  Atendido
                </button>
                <button
                  @click="cancelarTurno(item)"
                  :disabled="item.estado !== 'RESERVADO'"
                  class="bg-red-600 hover:bg-red-700 disabled:bg-slate-300 text-white font-semibold px-3 py-2 rounded text-xs"
                >
                  Cancelar
                </button>
              </div>

              <div v-if="modo === 'disponibilidades'" class="flex gap-2">
                <button
                  @click="editarDisponibilidad(item)"
                  class="bg-slate-700 hover:bg-slate-800 text-white font-semibold px-3 py-2 rounded text-xs"
                >
                  Editar
                </button>
                <button
                  @click="eliminarDisponibilidad(item)"
                  class="bg-red-600 hover:bg-red-700 text-white font-semibold px-3 py-2 rounded text-xs"
                >
                  Eliminar
                </button>
              </div>
            </div>
          </article>
        </div>

        <p v-else class="p-5 text-sm text-slate-500">
          Todavia no hay datos para mostrar. Elegi una opcion del panel.
        </p>
      </section>
    </main>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useTurnosStore } from '../stores/turnos'
import api from '../services/api'

const router = useRouter()
const store = useTurnosStore()

// Estado del panel: listado actual, mensajes, modo seleccionado y formulario.
const items = ref([])
const error = ref('')
const mensaje = ref('')
const tituloListado = ref('Resumen')
const modo = ref('')
const fechaAgenda = ref('')
const mostrarFormulario = ref(false)
const ciudades = ref([])
const establecimientos = ref([])
const especialidades = ref([])
const ciudadSeleccionada = ref('')
const disponibilidadEditandoId = ref(null)

const form = ref({
  establecimiento_id: '',
  especialidad_id: '',
  dia_semana: '',
  hora_inicio: '',
  hora_fin: '',
  duracion_turno_minutos: 30,
})

onMounted(async () => {
  // Las ciudades permiten construir los selectores dependientes del formulario.
  await cargarCiudades()
})

// Carga encadenada de catálogos. Al cambiar un nivel se invalidan los niveles
// inferiores para evitar combinaciones que ya no pertenecen entre sí.
const cargarCiudades = async () => {
  try {
    const respuesta = await api.get('ciudades/')
    ciudades.value = respuesta.data
  } catch (err) {
    error.value = 'No se pudieron cargar las ciudades.'
  }
}

const cargarEstablecimientos = async () => {
  form.value.establecimiento_id = ''
  form.value.especialidad_id = ''
  establecimientos.value = []
  especialidades.value = []

  if (!ciudadSeleccionada.value) return

  try {
    const respuesta = await api.get('establecimientos/', {
      params: {
        ciudad_id: ciudadSeleccionada.value,
      },
    })

    establecimientos.value = respuesta.data
  } catch (err) {
    error.value = 'No se pudieron cargar los establecimientos.'
  }
}

const cargarEspecialidades = async () => {
  form.value.especialidad_id = ''
  especialidades.value = []

  if (!form.value.establecimiento_id) return

  try {
    const respuesta = await api.get('especialidades/', {
      params: {
        establecimiento_id: form.value.establecimiento_id,
      },
    })

    especialidades.value = respuesta.data
  } catch (err) {
    error.value = 'No se pudieron cargar las especialidades.'
  }
}

const cargarDatos = async (titulo, endpoint, nuevoModo) => {
  // Unifica la carga de turnos, turnos activos y disponibilidades, además de
  // preparar el título y las acciones que debe mostrar cada fila.
  error.value = ''
  mensaje.value = ''
  tituloListado.value = titulo
  modo.value = nuevoModo

  try {
    const respuesta = await api.get(endpoint)
    items.value = respuesta.data
  } catch (err) {
    items.value = []
    error.value = err.response?.data?.error || 'No se pudieron cargar los datos.'
  }
}

const cargarTurnos = () => cargarDatos('Mis turnos', 'medico/mis_turnos/', 'turnos')
const cargarTurnosActivos = () => cargarDatos('Turnos activos', 'medico/mis_turnos/activos/', 'turnos')
const cargarDisponibilidades = () => cargarDatos('Disponibilidades', 'medico/disponibilidades/', 'disponibilidades')

const cargarAgendaPorFecha = async () => {
  await cargarDatos('Agenda por fecha', `medico/agenda/?fecha=${fechaAgenda.value}`, 'turnos')
}

// Acciones de estado sobre turnos. ejecutarAccion concentra POST, mensajes y
// recarga del listado para mantener consistentes todas las vistas.
const marcarAtendido = async (turno) => {
  await ejecutarAccion(`medico/turnos/${turno.id}/atendido/`, 'Turno marcado como atendido.')
}

const cancelarTurno = async (turno) => {
  const confirmado = window.confirm(
    `¿Confirmas que deseas cancelar el turno del ${turno.fecha} a las ${turno.hora?.slice(0, 5)}?`,
  )

  if (!confirmado) return

  await ejecutarAccion(`medico/turnos/${turno.id}/cancelar/`, 'Turno cancelado.')
}

const ejecutarAccion = async (endpoint, textoOk) => {
  error.value = ''
  mensaje.value = ''

  try {
    await api.post(endpoint)
    mensaje.value = textoOk
    await recargarListadoActual()
  } catch (err) {
    error.value = err.response?.data?.error || 'No se pudo realizar la accion.'
  }
}

const eliminarDisponibilidad = async (disponibilidad) => {
  // El horario se incluye en el mensaje para reducir eliminaciones accidentales.
  const confirmado = window.confirm(
    `¿Confirmas que deseas eliminar la disponibilidad del ${nombreDia(disponibilidad.dia_semana)} de ${disponibilidad.hora_inicio?.slice(0, 5)} a ${disponibilidad.hora_fin?.slice(0, 5)}?`,
  )

  if (!confirmado) return

  error.value = ''
  mensaje.value = ''

  try {
    await api.delete(`medico/disponibilidades/${disponibilidad.id}/eliminar/`)
    mensaje.value = 'Disponibilidad eliminada.'
    await cargarDisponibilidades()
  } catch (err) {
    error.value = err.response?.data?.error || 'No se pudo eliminar la disponibilidad.'
  }
}

const abrirFormularioNuevo = () => {
  // El mismo formulario se reutiliza para crear y editar; aquí se fuerza el modo alta.
  if (mostrarFormulario.value && !disponibilidadEditandoId.value) {
    mostrarFormulario.value = false
    return
  }

  limpiarFormularioDisponibilidad()
  mostrarFormulario.value = true
}

const editarDisponibilidad = async (disponibilidad) => {
  // Los catálogos se cargan en orden antes de asignar sus IDs, de modo que cada
  // select contenga la opción que debe mostrarse como elegida.
  error.value = ''
  mensaje.value = ''
  disponibilidadEditandoId.value = disponibilidad.id
  mostrarFormulario.value = true

  ciudadSeleccionada.value = disponibilidad.establecimiento?.ciudad?.id || ''
  await cargarEstablecimientos()

  form.value.establecimiento_id = disponibilidad.establecimiento?.id || ''
  await cargarEspecialidades()

  form.value.especialidad_id = disponibilidad.especialidad?.id || ''
  form.value.dia_semana = String(disponibilidad.dia_semana)
  form.value.hora_inicio = disponibilidad.hora_inicio?.slice(0, 5) || ''
  form.value.hora_fin = disponibilidad.hora_fin?.slice(0, 5) || ''
  form.value.duracion_turno_minutos = disponibilidad.duracion_turno_minutos

  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const guardarDisponibilidad = async () => {
  error.value = ''
  mensaje.value = ''

  try {
    // La presencia de un ID determina si corresponde PUT o POST.
    if (disponibilidadEditandoId.value) {
      await api.put(
        `medico/disponibilidades/${disponibilidadEditandoId.value}/modificar/`,
        form.value,
      )
      mensaje.value = 'Disponibilidad modificada.'
    } else {
      await api.post('medico/disponibilidades/crear/', form.value)
      mensaje.value = 'Disponibilidad creada.'
    }

    mostrarFormulario.value = false
    limpiarFormularioDisponibilidad()
    await cargarDisponibilidades()
  } catch (err) {
    error.value = err.response?.data?.error || 'No se pudo guardar la disponibilidad.'
  }
}

const limpiarFormularioDisponibilidad = () => {
  // Restablece tanto valores visibles como opciones dependientes y modo edición.
  disponibilidadEditandoId.value = null
  ciudadSeleccionada.value = ''
  establecimientos.value = []
  especialidades.value = []
  form.value = {
    establecimiento_id: '',
    especialidad_id: '',
    dia_semana: '',
    hora_inicio: '',
    hora_fin: '',
    duracion_turno_minutos: 30,
  }
}

const cancelarEdicion = () => {
  mostrarFormulario.value = false
  limpiarFormularioDisponibilidad()
}

const recargarListadoActual = async () => {
  // Después de una acción se conserva el contexto que el médico estaba mirando.
  if (tituloListado.value === 'Turnos activos') {
    await cargarTurnosActivos()
  } else if (tituloListado.value === 'Agenda por fecha' && fechaAgenda.value) {
    await cargarAgendaPorFecha()
  } else {
    await cargarTurnos()
  }
}

const tituloItem = (item) => {
  // Turnos y disponibilidades comparten la tarjeta, pero presentan datos distintos.
  if (modo.value === 'disponibilidades') {
    return `${item.especialidad?.nombre || 'Especialidad'} - ${item.establecimiento?.nombre || 'Establecimiento'}`
  }

  return `${item.especialidad?.nombre || 'Turno'} - ${nombrePaciente(item.usuario)}`
}

const detalleItem = (item) => {
  if (modo.value === 'disponibilidades') {
    return `${nombreDia(item.dia_semana)} de ${item.hora_inicio} a ${item.hora_fin} - ${item.duracion_turno_minutos} min`
  }

  return `${item.fecha} a las ${item.hora} - ${item.establecimiento?.nombre || ''}`
}

const nombrePaciente = (usuario) => {
  // Tolera respuestas antiguas donde usuario todavía podía ser solo un ID.
  if (!usuario || typeof usuario !== 'object') {
    return `Paciente #${usuario || 'sin identificar'}`
  }

  const nombreCompleto = `${usuario.first_name || ''} ${usuario.last_name || ''}`.trim()
  return nombreCompleto || usuario.username || `Paciente #${usuario.id}`
}

const detallePaciente = (usuario) => {
  if (!usuario || typeof usuario !== 'object') return ''

  return [usuario.username && `Usuario: ${usuario.username}`, usuario.email]
    .filter(Boolean)
    .join(' - ')
}

const nombreDia = (dia) => {
  const dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
  return dias[Number(dia)] || `Dia ${dia}`
}

const cerrarSesion = () => {
  store.cerrarSesion()
  router.push('/')
}
</script>
