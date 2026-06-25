<!-- Componente raíz: presenta la pantalla correspondiente a la ruta activa. -->
<template>
  <div class="min-h-screen bg-slate-50 font-sans antialiased">
    <RouterView />
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router'
</script>

<style>
body {
  margin: 0;
  padding: 0;
}
</style>
