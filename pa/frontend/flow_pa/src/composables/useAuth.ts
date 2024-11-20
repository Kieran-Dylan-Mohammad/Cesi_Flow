import { ref } from 'vue'

export function useAuth() {
  const isAuthenticated = ref(false)
  
  const login = async (username: string, password: string) => {
    try {
      // Appel API à implémenter
      const response = await fetch('http://localhost:8000/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      })
      
      if (response.ok) {
        isAuthenticated.value = true
        return true
      }
      return false
    } catch (error) {
      console.error('Erreur de connexion:', error)
      return false
    }
  }

  const logout = async () => {
    try {
      // Appel API à implémenter si nécessaire
      isAuthenticated.value = false
      return true
    } catch (error) {
      console.error('Erreur de déconnexion:', error)
      return false
    }
  }

  return {
    isAuthenticated,
    login,
    logout
  }
}
