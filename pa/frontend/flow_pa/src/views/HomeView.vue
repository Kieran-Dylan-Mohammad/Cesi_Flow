<template>
  <div class="home">
    <TheNavbar />
    
    <main>
      <section class="hero">
        <div class="container">
          <h1 class="hero__title">Flow PA</h1>
          <p class="hero__subtitle">
            Automatisation intelligente de vos Prosits CESI
          </p>
          <div class="hero__actions">
            <BaseButton 
              variant="primary"
              @click="$router.push('/login')"
            >
              Commencer
              <i class="fas fa-arrow-right"></i>
            </BaseButton>
          </div>
        </div>
      </section>
      
      <section class="features">
        <div class="container">
          <h2 class="section-title">Fonctionnalités</h2>
          <div class="features__grid">
            <div class="feature-card">
              <i class="fas fa-robot"></i>
              <h3>Automatisation Intelligente</h3>
              <p>Générez vos Prosits automatiquement grâce à l'IA</p>
            </div>
            
            <div class="feature-card">
              <i class="fas fa-bolt"></i>
              <h3>Rapide et Efficace</h3>
              <p>Gagnez du temps sur vos tâches administratives</p>
            </div>
            
            <div class="feature-card">
              <i class="fas fa-shield-alt"></i>
              <h3>Sécurisé</h3>
              <p>Vos données sont protégées et confidentielles</p>
            </div>
          </div>
        </div>
      </section>

      <section class="stats">
        <div class="container">
          <div class="stats__grid">
            <div class="stat-card">
              <div class="stat-number">500+</div>
              <div class="stat-label">Prosits Générés</div>
            </div>
            <div class="stat-card">
              <div class="stat-number">98%</div>
              <div class="stat-label">Satisfaction</div>
            </div>
            <div class="stat-card">
              <div class="stat-number">24/7</div>
              <div class="stat-label">Disponibilité</div>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup lang="ts">
import TheNavbar from '@/components/layout/TheNavbar.vue'
import BaseButton from '@/components/ui/BaseButton.vue'
</script>

<style src="@/styles/pages/home.css" scoped></style>
