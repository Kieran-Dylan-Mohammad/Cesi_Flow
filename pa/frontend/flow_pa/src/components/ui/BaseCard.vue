<template>
  <div 
    class="card" 
    :class="[
      `card--${variant}`,
      { 'card--hoverable': hoverable }
    ]"
  >
    <div v-if="$slots.header" class="card__header">
      <slot name="header"></slot>
    </div>

    <div class="card__body">
      <slot></slot>
    </div>

    <div v-if="$slots.footer" class="card__footer">
      <slot name="footer"></slot>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  variant?: 'flat' | 'elevated' | 'outlined'
  hoverable?: boolean
}>()
</script>

<style src="@/styles/components/card.css" scoped></style>
