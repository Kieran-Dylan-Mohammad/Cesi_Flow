<script setup lang="ts">
import { useRouter } from 'vue-router'
import BaseButton from '@/components/ui/BaseButton.vue'
import LoginForm from '@/components/auth/LoginForm.vue'

const router = useRouter()
</script>

<template>
  <div class="login-page">
    <div class="login-container">
      <BaseButton 
        variant="ghost"
        icon="arrow-left"
        @click="$router.push('/')"
        class="back-button"
      >
        Retour
      </BaseButton>

      <LoginForm />
    </div>
  </div>
</template>

<style src="@/styles/pages/login.css" scoped></style>
