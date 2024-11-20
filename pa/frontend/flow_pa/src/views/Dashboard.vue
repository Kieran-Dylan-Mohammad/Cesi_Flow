<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import BaseButton from '@/components/ui/BaseButton.vue'
import StatusCard from '@/components/dashboard/StatusCard.vue'
import ActionCard from '@/components/dashboard/ActionCard.vue'
import ProgressCard from '@/components/dashboard/ProgressCard.vue'
import ErrorCard from '@/components/dashboard/ErrorCard.vue'

const router = useRouter()
const loading = ref(false)
const error = ref('')
const message = ref('')
const currentStep = ref('')
const processingSteps = ref<string[]>([])

const startAutomation = async () => {
  loading.value = true
  error.value = ''
  processingSteps.value = []
  
  try {
    currentStep.value = 'Initialisation du processus...'
    processingSteps.value.push('Initialisation')
    
    const response = await axios.post('http://localhost:8000/api/complete-prosit')
    
    if (response.data.success) {
      message.value = 'Prosit complété avec succès!'
      processingSteps.value.push('Prosit complété')
    }
  } catch (e: any) {
    error.value = e.response?.data?.detail || 'Erreur lors de l\'automatisation'
    processingSteps.value.push('Erreur rencontrée')
  } finally {
    loading.value = false
    currentStep.value = ''
  }
}
</script>

<template>
  <div class="dashboard-container">
    <nav class="dashboard-nav">
      <img src="../assets/cesi-logo.png" alt="CESI" class="dashboard-nav__logo">
      <BaseButton
        variant="outline"
        icon="sign-out-alt"
        @click="router.push('/login')"
      >
        Déconnexion
      </BaseButton>
    </nav>

    <div class="dashboard-content">
      <StatusCard :loading="loading" />
      <ActionCard :loading="loading" @start="startAutomation" />
      <ProgressCard 
        v-if="processingSteps.length" 
        :steps="processingSteps" 
      />
      <ErrorCard 
        v-if="error" 
        :message="error" 
      />
    </div>
  </div>
</template>

<style src="@/styles/pages/dashboard.css" scoped></style>
