<template>
  <div class="home">
    <h1>Registro de Notificaciones 📩</h1>
    <NotificationForm />
  </div>
</template>

<script>
import NotificationForm from '../components/NotificationForm.vue'

export default {
  name: 'HomeView', //se le agrega nombre multi-palabra
  components: {
    NotificationForm,
  },
}
</script>
