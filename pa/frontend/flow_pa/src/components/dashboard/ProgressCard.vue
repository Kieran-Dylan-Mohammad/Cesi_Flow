<template>
  <BaseCard>
    <h2>Progression</h2>
    <ul class="steps-list">
      <li v-for="(step, index) in steps" :key="index">
        <i class="fas fa-check"></i>
        {{ step }}
      </li>
    </ul>
  </BaseCard>
</template>

<script setup lang="ts">
import BaseCard from '@/components/ui/BaseCard.vue'

defineProps<{
  steps: string[]
}>()
</script>
