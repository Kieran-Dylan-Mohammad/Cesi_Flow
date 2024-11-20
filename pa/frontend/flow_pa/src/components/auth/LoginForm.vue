<template>
  <BaseCard variant="elevated" class="login-form">
    <template #header>
      <div class="login-form__header">
        <img src="../../assets/cesi-logo.png" alt="CESI" class="login-form__logo">
        <h1 class="login-form__title">Connexion</h1>
      </div>
    </template>

    <form @submit.prevent="handleSubmit">
      <BaseInput
        id="username"
        v-model="form.username"
        label="Nom d'utilisateur"
        icon="user"
        :error="errors.username"
        :disabled="isLoading"
      />

      <BaseInput
        id="password"
        v-model="form.password"
        type="password"
        label="Mot de passe"
        icon="lock"
        :error="errors.password"
        :disabled="isLoading"
      >
        <template #suffix>
          <button 
            type="button"
            class="password-toggle"
            @click="togglePassword"
          >
            <i :class="['fas', showPassword ? 'fa-eye-slash' : 'fa-eye']"></i>
          </button>
        </template>
      </BaseInput>

      <BaseButton
        type="submit"
        variant="primary"
        :loading="isLoading"
        class="login-form__submit"
      >
        Se connecter
      </BaseButton>
    </form>
  </BaseCard>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuth } from '@/composables/useAuth'
import BaseButton from '../ui/BaseButton.vue'
import BaseInput from '../ui/BaseInput.vue'
import BaseCard from '../ui/BaseCard.vue'

const router = useRouter()
const { login } = useAuth()

const form = ref({
  username: '',
  password: ''
})

const errors = ref({
  username: '',
  password: ''
})

const isLoading = ref(false)
const showPassword = ref(false)

const togglePassword = () => {
  showPassword.value = !showPassword.value
}

const handleSubmit = async () => {
  isLoading.value = true
  errors.value = { username: '', password: '' }

  try {
    const success = await login(form.value.username, form.value.password)
    if (success) {
      router.push('/dashboard')
    } else {
      errors.value.password = 'Identifiants incorrects'
    }
  } catch (error) {
    console.error('Erreur de connexion:', error)
    errors.value.password = 'Une erreur est survenue'
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped>
.login-form {
  width: 100%;
}

.login-form__header {
  text-align: center;
  margin-bottom: var(--spacing-lg);
}

.login-form__logo {
  width: 120px;
  margin-bottom: var(--spacing-md);
}

.login-form__title {
  font-size: 1.5rem;
  color: var(--color-gray-900);
}

.login-form__submit {
  width: 100%;
  margin-top: var(--spacing-lg);
}

.password-toggle {
  background: none;
  border: none;
  color: var(--color-gray-500);
  cursor: pointer;
}
</style>
