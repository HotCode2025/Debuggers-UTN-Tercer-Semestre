<!-- Navegación compartida por las pantallas principales del paciente. -->
<template>
  <nav class="bg-teal-600 text-white px-6 py-3 shadow flex justify-between items-center font-sans">
    <div class="flex items-center space-x-2 cursor-pointer" @click="router.push('/home')">
      <img
  src="/src/assets/logo.png"
  alt="Mi Turnero"
  class="w-9 h-9 object-contain"
/>
      <span class="text-lg font-bold tracking-tight">Mi Turnero</span>
    </div>
    <div class="flex space-x-6 text-sm font-medium">
      <router-link to="/mis-turnos" class="hover:opacity-80 transition-opacity">Mis turnos</router-link>
      <router-link to="/" class="hover:opacity-80 transition-opacity">Mi cuenta</router-link>
    </div>
  </nav>
</template>

<script setup>
import { useRouter } from 'vue-router'

// El router se usa para que el logotipo funcione como acceso al inicio.
const router = useRouter()
</script>
