
<template>
    <form @submit.prevent="submitForm">
      <label>Fecha de recepción</label>
      <input type="date" v-model="form.fecha_recepcion" required />
  
      <label>Hora de recepción</label>
      <input type="time" v-model="form.hora_recepcion" required />
  
      <label>Entidad emisora</label>
      <input type="text" v-model="form.entidad_emisora" required />
  
      <label>Número de expediente</label>
      <input type="text" v-model="form.numero_expediente" required />
  
      <label>Dirigido a</label>
      <input type="text" v-model="form.dirigido_a" required />
  
      <label>Recepcionista</label>
      <select v-model="form.recepcionista" required>
        <option>Amanda González</option>
        <option>Wanda Pastor</option>
      </select>
  
      <label>Fecha de entrega</label>
      <input type="date" v-model="form.fecha_entrega" required />
  
      <label>Hora de entrega</label>
      <input type="time" v-model="form.hora_entrega" required />
  
      <label>Entregado a (ID usuario)</label>
      <input type="number" v-model="form.entregado_a" required />
  
      <button type="submit">Enviar Notificación</button>
    </form>
  </template>
  
  <script>
  import api from '../services/api'
  
  export default {
    name: 'NotificationForm',
    data() {
      return {
        form: {
          fecha_recepcion: '',
          hora_recepcion: '',
          entidad_emisora: '',
          numero_expediente: '',
          dirigido_a: '',
          recepcionista: '',
          fecha_entrega: '',
          hora_entrega: '',
          entregado_a: '', // ID del usuario, puedes hacer un select dinámico si prefieres
        },
      }
    },
    methods: {
      async submitForm() {
        try {
          const res = await api.post('/notificaciones/', this.form)
          alert('Notificación registrada correctamente')
          console.log(res.data)
        } catch (error) {
          alert('Ocurrió un error al enviar la notificación')
          console.error(error)
        }
      },
    },
  }
  </script>
  
  <style scoped>
  form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    max-width: 600px;
    margin: 2rem auto;
  }
  </style>
  