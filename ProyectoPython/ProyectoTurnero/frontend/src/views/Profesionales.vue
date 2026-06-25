<!-- Tercer paso de la reserva: selección del profesional habilitado. -->
<template>
  <div class="min-h-screen bg-slate-100 font-sans antialiased flex flex-col">
    <header class="bg-white border-b border-slate-200 px-6 py-4 shadow-sm flex items-center justify-between">
      <div class="flex items-center space-x-3">
        <img src="/src/assets/logo.png" alt="Mi Turnero" class="w-12 h-12 object-contain" />
        <div>
          <h1 class="text-xl font-bold tracking-tight text-slate-900">Mi Turnero</h1>
          <span class="text-xs text-slate-500">Profesionales de la salud</span>
        </div>
      </div>
      <button @click="router.push('/especialidades')" class="text-sm font-semibold text-teal-600 hover:underline">
        Volver
      </button>
    </header>

    <main class="flex-grow max-w-2xl w-full mx-auto p-6">
      <div class="mb-4">
        <span class="text-xs bg-teal-50 text-teal-700 font-bold px-2.5 py-1 rounded-full border border-teal-200">
          {{ store.turnoProceso.especialidad?.nombre || 'Especialidad' }}
        </span>
        <h2 class="text-xl font-bold text-slate-800 mt-3">Medicos disponibles</h2>
      </div>

      <p v-if="error" class="bg-red-50 text-red-700 p-3 rounded-lg border border-red-200 text-xs font-semibold mb-4">
        {{ error }}
      </p>

      <div v-if="profesionales.length" class="space-y-3">
        <div
          v-for="doc in profesionales"
          :key="doc.id"
          class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex justify-between items-center"
        >
          <div>
            <h3 class="font-bold text-slate-900 text-lg">{{ doc.nombre }}</h3>
            <p class="text-sm text-teal-600 font-medium">
              {{ store.turnoProceso.especialidad?.nombre }}
            </p>
          </div>
          <button
            @click="seleccionarProfesional(doc)"
            class="bg-teal-600 hover:bg-teal-700 text-white text-sm font-semibold px-4 py-2 rounded shadow-sm"
          >
            Agendar turno
          </button>
        </div>
      </div>

      <p v-else-if="!error" class="text-sm text-slate-500">
        No hay profesionales cargados para esta especialidad.
      </p>
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

// Profesionales habilitados para la combinación seleccionada.
const profesionales = ref([])
const error = ref('')

onMounted(async () => {
  // Centro y especialidad son requisitos del endpoint de profesionales.
  const establecimiento = store.turnoProceso.establecimiento
  const especialidad = store.turnoProceso.especialidad

  if (!establecimiento?.id || !especialidad?.id) {
    router.push('/centros')
    return
  }

  try {
    const respuesta = await api.get('profesionales/', {
      params: {
        establecimiento_id: establecimiento.id,
        especialidad_id: especialidad.id,
      },
    })

    profesionales.value = respuesta.data
  } catch (err) {
    error.value = 'No se pudieron cargar los profesionales.'
  }
})

const seleccionarProfesional = (profesional) => {
  // Completa el contexto mínimo necesario para consultar disponibilidad real.
  store.turnoProceso.profesional = profesional
  store.turnoProceso.fecha = ''
  store.turnoProceso.hora = ''
  router.push('/confirmar')
}
</script>
