<!-- Tarjeta reutilizable para presentar centros u opciones con contenido adicional. -->
<template>
  <div class="bg-white p-5 rounded-xl shadow-sm border border-slate-100 flex justify-between items-center hover:shadow-md transition-shadow">
    <div class="space-y-1">
      <div class="flex items-center space-x-2">
        <span class="text-xl">{{ icono }}</span>
        <h3 class="text-lg font-bold text-slate-700">{{ titulo }}</h3>
      </div>
      <p v-if="subtitulo" class="text-sm text-slate-400 pl-7">{{ subtitulo }}</p>
      <p v-if="infoExtra" class="text-xs text-teal-600 font-medium pl-7">{{ infoExtra }}</p>
    </div>
    <div>
      <slot></slot>
    </div>
  </div>
</template>

<script setup>
// Las props describen el contenido estable; el slot permite insertar una acción
// distinta sin duplicar la estructura visual de la tarjeta.
defineProps({
  titulo: { type: String, required: true },
  subtitulo: { type: String, default: '' },
  infoExtra: { type: String, default: '' },
  icono: { type: String, default: '🏢' }
})
</script>
