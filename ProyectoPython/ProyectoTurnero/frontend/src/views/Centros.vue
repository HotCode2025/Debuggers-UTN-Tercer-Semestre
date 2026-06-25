<!-- Primer paso de la reserva: selección de ciudad y establecimiento. -->
<template>
  <div class="min-h-screen bg-slate-100 font-sans antialiased flex flex-col">
    
    <header class="bg-white border-b border-slate-200 px-6 py-4 shadow-sm flex items-center justify-between">
      <div class="flex items-center space-x-3">
        <img src="/src/assets/logo.png" alt="Mi Turnero" class="w-12 h-12 object-contain" />
        <div>
          <h1 class="text-xl font-bold tracking-tight text-slate-900">Mi Turnero</h1>
          <span class="text-xs text-slate-500">Centros Médicos Autorizados</span>
        </div>
      </div>
      <button @click="router.push('/home')" class="text-sm font-semibold text-teal-600 hover:underline">
        ← Volver al Menú
      </button>
    </header>

    <main class="flex-grow max-w-4xl w-full mx-auto p-6">
      <!-- FILTROS GEOGRÁFICOS -->
      <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm mb-6">
        <h2 class="text-lg font-bold text-slate-800 mb-4">Filtrar por ubicación real</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
              <label class="block text-xs font-bold uppercase text-slate-500 mb-1">
              Ciudad
            </label>

  <select
    v-model="ciudadSeleccionada"
    @change="cargarCentros"
    class="w-full border border-slate-300 p-2.5 rounded text-sm"
  >
    <option value="" disabled>Seleccione una ciudad</option>

    <option
      v-for="ciudad in ciudades"
      :key="ciudad.id"
      :value="ciudad.id"
    >
      {{ ciudad.nombre }}, {{ ciudad.provincia }}
    </option>
  </select>
</div>
            
        </div>
      </div>

      <!-- LISTADO VINCULADO A LOS CENTROS REALES DE TU STORE -->
      <div class="space-y-4">
        <h3 class="text-sm font-bold uppercase tracking-wider text-slate-400">Efectores en {{ ciudadSeleccionada }}</h3>
        
        <div v-for="centro in centros" :key="centro.id" class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex justify-between items-center hover:border-teal-500 transition-colors">
          <div>
            <h4 class="font-bold text-slate-900 text-lg">{{ centro.nombre }}</h4>
            <p class="text-sm text-slate-500">{{ centro.direccion }} • Tel: {{ centro.tel }}</p>
          </div>
          <button @click="seleccionarCentro(centro)" class="bg-teal-600 hover:bg-teal-700 text-white text-sm font-semibold px-4 py-2 rounded shadow-sm">
            Ver Turnos
          </button>
        </div>
      </div>
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

// Catálogos remotos y valor elegido en el filtro geográfico.
const ciudades = ref([])
const centros = ref([])
const ciudadSeleccionada = ref('')

onMounted(async () => {
  // La ciudad es el primer nivel del catálogo y se carga al abrir la pantalla.
  const respuesta = await api.get('ciudades/')
  ciudades.value = respuesta.data
})

const cargarCentros = async () => {
  // Sin ciudad no existe una consulta válida y se limpia el resultado anterior.
  if (!ciudadSeleccionada.value) {
    centros.value = []
    return
  }

  const respuesta = await api.get('establecimientos/', {
    params: {
      ciudad_id: ciudadSeleccionada.value,
    },
  })

  centros.value = respuesta.data
}

const seleccionarCentro = (centro) => {
  // Se conserva el objeto completo para mostrar sus datos en pasos posteriores.
  store.turnoProceso.establecimiento = centro
  router.push('/especialidades')
}
</script>
