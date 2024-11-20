<template>
  <BaseCard>
    <h2>Actions Disponibles</h2>
    <BaseButton
      variant="primary"
      :loading="loading"
      @click="$emit('start')"
      class="action-button"
    >
      <i class="fas fa-play"></i>
      {{ loading ? 'Traitement en cours...' : 'Démarrer l\'automatisation' }}
    </BaseButton>
  </BaseCard>
</template>

<script setup lang="ts">
import BaseCard from '@/components/ui/BaseCard.vue'
import BaseButton from '@/components/ui/BaseButton.vue'

defineProps<{
  loading: boolean
}>()
</script>
