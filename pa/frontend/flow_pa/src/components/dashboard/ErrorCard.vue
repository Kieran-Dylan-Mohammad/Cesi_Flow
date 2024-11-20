<template>
  <BaseCard>
    <div class="error-message">
      <i class="fas fa-exclamation-circle"></i>
      <span>{{ message }}</span>
    </div>
  </BaseCard>
</template>

<script setup lang="ts">
import BaseCard from '@/components/ui/BaseCard.vue'

defineProps<{
  message: string
}>()
</script>

<style scoped>
.error-message {
  color: var(--color-danger);
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
}
</style>
