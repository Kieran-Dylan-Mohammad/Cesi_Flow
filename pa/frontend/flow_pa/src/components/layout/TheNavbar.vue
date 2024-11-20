<template>
  <nav class="navbar">
    <div class="navbar__content">
      <router-link to="/" class="navbar__logo">
        <AppLogo :small="isSmallScreen" />
      </router-link>
      
      <div class="navbar__actions">
        <template v-if="isAuthenticated">
          <BaseButton variant="ghost" @click="$router.push('/dashboard')">
            <i class="fas fa-chart-line"></i>
            Dashboard
          </BaseButton>
          <BaseButton variant="primary" @click="handleLogout">
            <i class="fas fa-sign-out-alt"></i>
            Déconnexion
          </BaseButton>
        </template>
        <template v-else>
          <BaseButton variant="primary" @click="$router.push('/login')">
            <i class="fas fa-sign-in-alt"></i>
            Connexion
          </BaseButton>
        </template>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { useAuth } from '@/composables/useAuth'
import BaseButton from '../ui/BaseButton.vue'
import AppLogo from '../ui/AppLogo.vue'

const router = useRouter()
const { isAuthenticated, logout } = useAuth()

const handleLogout = async () => {
  await logout()
  router.push('/login')
}
</script>

<style src="@/styles/components/navbar.css" scoped></style>
    
