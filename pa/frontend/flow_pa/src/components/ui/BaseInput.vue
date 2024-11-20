<template>
  <div class="input-wrapper" :class="{ 'has-error': error }">
    <label v-if="label" :for="id" class="input-label">
      {{ label }}
    </label>
    
    <div class="input-container">
      <i v-if="icon" :class="['fas', `fa-${icon}`, 'input-icon']"></i>
      
      <input
        :id="id"
        :type="type"
        :value="modelValue"
        :disabled="disabled"
        class="input-field"
        v-bind="$attrs"
        @input="$emit('update:modelValue', ($event.target as HTMLInputElement).value)"
      >
      
      <slot name="suffix"></slot>
    </div>

    <p v-if="error" class="input-error">
      {{ error }}
    </p>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  id: string
  modelValue: string
  label?: string
  type?: string
  icon?: string
  error?: string
  disabled?: boolean
}>()

defineEmits<{
  'update:modelValue': [value: string]
}>()
</script>

<style src="@/styles/components/input.css" scoped></style>
