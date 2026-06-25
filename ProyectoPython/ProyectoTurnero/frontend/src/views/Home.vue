<!-- Menú principal del paciente y accesos a reserva e historial. -->
<template>
  <div class="min-h-screen bg-slate-100 font-sans antialiased text-slate-800 flex flex-col">
    
    <!-- HEADER INSTITUCIONAL CON LOGO -->
    <header class="bg-white border-b border-slate-200 px-6 py-4 shadow-sm flex items-center justify-between">
      <div class="flex items-center space-x-3">
        <img src="/src/assets/logo.png" alt="Mi Turnero" class="w-12 h-12 object-contain" />
        <div>
          <h1 class="text-xl font-bold tracking-tight text-slate-900 leading-none">Mi Turnero</h1>
          <span class="text-xs text-slate-500">Sistema Institucional de Turnos</span>
        </div>
      </div>
      <div class="text-right text-sm">
        <p class="font-medium text-slate-700">Hola, {{ store.usuario.nombre || 'Paciente' }}</p>
        <button @click="cerrarSesion" class="text-xs text-red-600 hover:underline font-semibold mt-0.5 block ml-auto">
          Cerrar sesión
        </button>
      </div>
    </header>

    <!-- CONTENIDO PRINCIPAL -->
    <main class="flex-grow max-w-4xl w-full mx-auto p-6 flex flex-col justify-center">
      
      <div class="text-center mb-8">
        <h2 class="text-2xl font-bold text-slate-800 mb-2">¿Qué turno desea gestionar hoy?</h2>
        <p class="text-slate-500 text-sm max-w-md mx-auto">Seleccione la categoría correspondiente para iniciar la búsqueda y reserva de su cita médica.</p>
      </div>

      <!-- BOTONERA REESTRUCTURADA -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

        <button @click="router.push('/mis-turnos')" class="md:col-span-2 bg-white p-5 rounded-xl border border-slate-200 shadow-sm hover:shadow-md hover:border-teal-500 transition-all text-left flex items-center justify-between gap-4 group">
          <div class="flex items-center gap-4">
            <div class="p-3 bg-teal-50 rounded-lg group-hover:bg-teal-100 text-teal-600 transition-colors">
              <svg class="w-8 h-8" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path d="M8 2v3m8-3v3M3 9h18M5 4h14a2 2 0 012 2v13a2 2 0 01-2 2H5a2 2 0 01-2-2V6a2 2 0 012-2zm3 9h3m-3 4h6" />
              </svg>
            </div>
            <div>
              <h3 class="font-bold text-lg text-slate-800 group-hover:text-teal-700">Mis turnos</h3>
              <p class="text-xs text-slate-400 mt-0.5">Consulta tus turnos reservados, atendidos y cancelados.</p>
            </div>
          </div>
          <span class="text-teal-600 text-2xl" aria-hidden="true">›</span>
        </button>
        
        <!-- BOTÓN ESPECIALIDADES -->
        <button @click="router.push('/especialidades')" class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm hover:shadow-md hover:border-teal-500 transition-all text-left flex items-center space-x-4 group">
          <div class="p-3 bg-teal-50 rounded-lg group-hover:bg-teal-100 text-teal-600 transition-colors">
            <!-- Icono Estetoscopio SVG real -->
            <svg class="w-8 h-8" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M14 10h.01M10 14h.01M12 12h.01M12 7c-2.76 0-5 2.24-5 5v3c0 .55.45 1 1 1h8c.55 0 1-.45 1-1v-3c0-2.76-2.24-5-5-5zM21 16.5c0 .83-.67 1.5-1.5 1.5h-15C3.67 18 3 17.33 3 16.5V11c0-4.97 4.03-9 9-9s9 4.03 9 9v5.5z"/></svg>
          </div>
          <div>
            <h3 class="font-bold text-lg text-slate-800 group-hover:text-teal-700">Especialidades Médicas</h3>
            <p class="text-xs text-slate-400 mt-0.5">Pediatría, Cardiología, Traumatología y más.</p>
          </div>
        </button>

        <!-- BOTÓN PROFESIONALES -->
        <button @click="router.push('/profesionales')" class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm hover:shadow-md hover:border-teal-500 transition-all text-left flex items-center space-x-4 group">
          <div class="p-3 bg-teal-50 rounded-lg group-hover:bg-teal-100 text-teal-600 transition-colors">
            <!-- Icono Doctor SVG real -->
            <svg class="w-8 h-8" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
          </div>
          <div>
            <h3 class="font-bold text-lg text-slate-800 group-hover:text-teal-700">Profesionales Médicos</h3>
            <p class="text-xs text-slate-400 mt-0.5">Busque a su médico de cabecera por nombre.</p>
          </div>
        </button>

        <!-- BOTÓN DESTACADO Y CENTRADO: HOSPITALES / CLÍNICAS -->
        <button @click="router.push('/centros')" class="md:col-span-2 bg-gradient-to-r from-teal-600 to-cyan-600 text-white p-6 rounded-xl shadow-md hover:from-teal-700 hover:to-cyan-700 transition-all flex flex-col items-center text-center group mt-2">
          <div class="p-3 bg-white/10 rounded-full mb-3 group-hover:scale-105 transition-transform">
            <!-- Icono Edificio Hospital SVG real -->
            <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
          </div>
          <h3 class="font-black text-xl tracking-wide uppercase leading-tight">
            Hospitales<br>Centros de Salud<br>Clínicas
          </h3>
          <p class="text-xs text-teal-100 mt-2 max-w-sm">Encuentre los efectores de salud públicos y privados más cercanos a su domicilio actual.</p>
        </button>

      </div>
    </main>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useTurnosStore } from '../stores/turnos'

const router = useRouter()
const store = useTurnosStore()

// Cerrar sesión limpia Pinia y los tokens antes de volver a la ruta pública.
const cerrarSesion = () => {
  store.cerrarSesion()
  router.push('/')
}
</script>
