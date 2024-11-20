<template>
  <BaseCard>
    <h2>État du Système</h2>
    <div class="status-indicator" :class="{ active: !loading }">
      <i class="fas fa-check-circle"></i>
      <span>Système prêt</span>
    </div>
  </BaseCard>
</template>

<script setup lang="ts">
import BaseCard from '@/components/ui/BaseCard.vue'

defineProps<{
  loading: boolean
}>()
</script>

<style scoped>
.status-indicator {
  display: flex;
  align-items: center;
  gap: var(--spacing-sm);
  color: var(--color-success);
  margin-top: var(--spacing-md);
}
</style>
