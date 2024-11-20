<template>
  <button
    :type="type"
    :disabled="disabled || loading"
    class="btn"
    :class="[
      `btn--${variant}`,
      { 'btn--loading': loading }
    ]"
  >
    <div class="btn__content" :class="{ 'btn__content--hidden': loading }">
      <i v-if="icon" :class="['fas', `fa-${icon}`, 'btn__icon']"></i>
      <slot></slot>
    </div>
    
    <div v-if="loading" class="btn__loader">
      <i class="fas fa-circle-notch fa-spin"></i>
    </div>
  </button>
</template>

<script setup lang="ts">
defineProps<{
  variant?: 'primary' | 'secondary' | 'outline' | 'ghost'
  type?: 'button' | 'submit'
  icon?: string
  loading?: boolean
  disabled?: boolean
}>()
</script>

<style src="@/styles/components/button.css" scoped></style>
