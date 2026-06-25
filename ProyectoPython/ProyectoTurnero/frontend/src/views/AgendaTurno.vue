<!-- Vista heredada de selección de fecha; no participa del flujo principal actual. -->
<template>
  <div class="min-h-screen bg-slate-50 font-sans text-slate-800">
    <Navbar />
    <div class="max-w-xl mx-auto pt-8 px-4 pb-12">
      <button @click="router.back()" class="text-sm text-teal-600 font-semibold mb-4 hover:underline flex items-center">
        ← Volver
      </button>

      <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-200 mb-6">
        <h2 class="text-lg font-bold text-slate-900 mb-4">Elegir fecha del turno</h2>
        
        <div class="space-y-4">
          <div>
            <label class="block text-xs font-bold uppercase text-slate-500 mb-1">Especialidad</label>
            <select v-model="store.turnoProceso.especialidad" class="w-full border border-slate-300 p-2.5 rounded text-sm bg-white outline-none">
              <option value="">Desplegable con especialidades típicas</option>
              <option value="Cardiología">Cardiología</option>
              <option value="Pediatría">Pediatría</option>
              <option value="Odontología">Odontología</option>
            </select>
          </div>

          <div>
            <label class="block text-xs font-bold uppercase text-slate-500 mb-1">Fechas disponibles</label>
            <input type="date" v-model="store.turnoProceso.fecha" class="w-full border border-slate-300 p-2.5 rounded text-sm outline-none focus:border-teal-500" />
          </div>

          <div>
            <label class="block text-xs font-bold uppercase text-slate-500 mb-2">Horarios disponibles</label>
            <div class="grid grid-cols-2 gap-3">
              <label v-for="hora in ['08:30', '10:20', '14:15', '16:00']" :key="hora" class="flex items-center space-x-2 border border-slate-200 p-2.5 rounded cursor-pointer hover:bg-slate-50 transition-colors">
                <input type="radio" :value="hora" v-model="store.turnoProceso.hora" class="accent-teal-600" />
                <span class="text-sm font-medium text-slate-700">{{ hora }} hs</span>
              </label>
            </div>
          </div>
        </div>
      </div>

      <div v-if="store.turnoProceso.fecha && store.turnoProceso.hora" class="bg-white p-6 rounded-xl shadow-sm border border-slate-200">
        <h2 class="text-xl font-bold text-slate-900 mb-4">Confirmar turno</h2>
        
        <div class="mb-6">
          <h3 class="text-sm font-bold text-slate-400 uppercase tracking-wider mb-2">Mis datos</h3>
          <div class="flex justify-between items-start text-sm bg-slate-50 p-4 rounded-lg border border-slate-100">
            <div>
              <p class="text-xs text-slate-400 font-semibold">Email</p>
              <p class="font-medium text-slate-800 mb-2">{{ store.usuario.email || 'hola@gmail.com' }}</p>
              <p class="text-xs text-slate-400 font-semibold">Teléfono</p>
              <p class="font-medium text-slate-800">{{ store.usuario.tel || '11-1234-5678' }}</p>
            </div>
            <button @click="router.push('/')" class="bg-slate-200 text-slate-700 px-3 py-1 rounded text-xs font-bold hover:bg-slate-300">
              Editar datos
            </button>
          </div>
        </div>

        <div class="border-t border-slate-100 pt-4 space-y-4 text-sm">
          <h3 class="text-sm font-bold text-slate-400 uppercase tracking-wider">Turno</h3>
          <div class="grid grid-cols-2 gap-4">
            <div>
              <p class="text-xs text-slate-400 font-semibold">Ubicación</p>
              <p class="font-bold text-slate-800">{{ store.turnoProceso.centro?.nombre || 'Hospital Juan Merenguito' }}</p>
              <p class="text-slate-500 text-xs">{{ store.turnoProceso.centro?.direccion || 'Avenida Pepito 113, Ciudad, Provincia' }}</p>
            </div>
            <div>
              <p class="text-xs text-slate-400 font-semibold">Cardiología</p>
              <p class="font-medium text-slate-800">{{ store.turnoProceso.profesional?.nombre || 'Dra Maria Julia Perez' }}</p>
            </div>
          </div>
          <div class="grid grid-cols-2 gap-4 pt-2">
            <div>
              <p class="text-xs text-slate-400 font-semibold">Teléfono</p>
              <p class="text-slate-700 font-medium">{{ store.turnoProceso.centro?.tel || '0800-123-1234' }}</p>
            </div>
            <div>
              <p class="text-xs text-slate-400 font-semibold">Día y horario</p>
              <p class="text-slate-700 font-bold">Viernes 05 de junio a las {{ store.turnoProceso.hora }} hs</p>
            </div>
          </div>
        </div>

        <div class="flex space-x-4 mt-8">
          <button @click="confirmar" class="w-1/2 bg-slate-800 hover:bg-slate-900 text-white font-bold py-2.5 rounded text-sm transition-colors shadow-sm">
            Confirmar turno
          </button>
          <button @click="router.push('/home')" class="w-1/2 bg-white border border-slate-300 hover:bg-slate-50 text-slate-700 font-bold py-2.5 rounded text-sm transition-colors">
            Cancelar
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import Navbar from '../components/Navbar.vue'
import { useRouter } from 'vue-router'
import { useTurnosStore } from '../stores/turnos'

const router = useRouter()
const store = useTurnosStore()

const confirmar = () => {
  store.confirmarTurnoActual()
  router.push('/mis-turnos')
}
</script>
