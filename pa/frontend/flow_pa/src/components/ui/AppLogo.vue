<template>
  <div class="app-logo" :class="{ 'app-logo--small': small }">
    <img 
      src="@/assets/cesi-logo.png" 
      alt="CESI" 
      class="app-logo__image"
    >
    <div v-if="!small" class="app-logo__text">
      <span class="app-logo__brand">Flow PA</span>
      <span class="app-logo__tagline">Automatisation CESI</span>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  small?: boolean
}>()
</script>
