<!-- Vista heredada de centros conservada como referencia del diseño inicial. -->
<template>
  <div class="min-h-screen bg-slate-50 font-sans text-slate-800">
    <Navbar />
    <div class="max-w-xl mx-auto pt-8 px-4 pb-12">
      <button @click="router.back()" class="text-sm text-teal-600 font-semibold mb-4 hover:underline flex items-center">
        ← Volver
      </button>

      <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
        <h2 class="text-lg font-bold text-slate-900 mb-4 capitalize">Hospitales | Centros de Salud | Clínicas</h2>
        
        <div class="mb-6 bg-slate-50 p-4 rounded-lg border border-slate-100">
          <p class="text-xs font-bold uppercase text-slate-400 mb-2">Elegir cercanía a</p>
          <div class="flex space-x-6 text-sm">
            <label class="flex items-center space-x-2 cursor-pointer">
              <input type="radio" value="direccion" v-model="cercania" class="accent-teal-600" />
              <span class="font-medium text-slate-700">Mi dirección</span>
            </label>
            <label class="flex items-center space-x-2 cursor-pointer">
              <input type="radio" value="ciudad" v-model="cercania" class="accent-teal-600" />
              <span class="font-medium text-slate-700">Ciudad / Provincia</span>
            </label>
          </div>
        </div>

        <div v-if="cercania === 'direccion'" class="space-y-4">
          <div>
            <label class="block text-xs font-bold uppercase text-slate-500 mb-1">Lugar de atención</label>
            <select v-model="lugarSeleccionado" class="w-full border border-slate-300 p-2.5 rounded bg-white text-sm outline-none focus:border-teal-500">
              <option value="">Seleccionar lugar de atención</option>
              <option v-for="centro in store.centros" :key="centro.id" :value="centro">
                {{ centro.nombre }} (A pocas cuadras)
              </option>
            </select>
          </div>
        </div>

        <div v-else class="space-y-4">
          <div>
            <label class="block text-xs font-bold uppercase text-slate-500 mb-1">Provincia</label>
            <select class="w-full border border-slate-300 p-2.5 rounded bg-white text-sm outline-none">
              <option>Seleccionar provincia</option>
              <option selected>Buenos Aires</option>
            </select>
          </div>
          <div>
            <label class="block text-xs font-bold uppercase text-slate-500 mb-1">Ciudad</label>
            <select class="w-full border border-slate-300 p-2.5 rounded bg-white text-sm outline-none">
              <option>Seleccionar ciudad</option>
              <option selected>Avellaneda</option>
            </select>
          </div>
          <div>
            <label class="block text-xs font-bold uppercase text-slate-500 mb-1">Lugar de atención</label>
            <select v-model="lugarSeleccionado" class="w-full border border-slate-300 p-2.5 rounded bg-white text-sm outline-none focus:border-teal-500">
              <option value="">Seleccionar lugar de atención</option>
              <option v-for="centro in store.centros" :key="centro.id" :value="centro">
                {{ centro.nombre }} — {{ centro.direccion }}
              </option>
            </select>
          </div>
        </div>

        <button @click="avanzar" :disabled="!lugarSeleccionado" class="w-full bg-teal-600 hover:bg-teal-700 disabled:bg-slate-200 disabled:text-slate-400 text-white font-semibold py-2.5 rounded transition-colors text-sm shadow-sm mt-6">
          Continuar
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Navbar from '../components/Navbar.vue'
import { useRouter } from 'vue-router'
import { useTurnosStore } from '../stores/turnos'

const router = useRouter()
const store = useTurnosStore()

const cercania = ref('direccion')
const lugarSeleccionado = ref('')

const avanzar = () => {
  store.turnoProceso.centro = lugarSeleccionado.value
  store.turnoProceso.especialidad = 'Cardiología'
  store.turnoProceso.profesional = store.profesionales[0]
  router.push('/agendar')
}
</script>
