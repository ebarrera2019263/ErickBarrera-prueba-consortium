<template>
  <div>
    <h2>📋 Notificaciones</h2>
    <button @click="showForm = true">Registrar Nueva Notificación</button>

    <!-- FORMULARIO -->
    <div v-if="showForm" style="margin: 20px 0; border: 1px solid #ccc; padding: 20px;">
      <form @submit.prevent="submitForm">
        <input v-model="form.entidad_emisora" placeholder="Entidad emisora" required />
        <input v-model="form.numero_expediente" placeholder="Número expediente" required />
        <input v-model="form.dirigido_a" placeholder="Dirigido a" required />
        <select v-model="form.recepcionista" required>
          <option value="">Recepcionista</option>
          <option value="amanda">Amanda González</option>
          <option value="wanda">Wanda Pastor</option>
        </select>
        <input type="date" v-model="form.fecha_recepcion" required />
        <input type="time" v-model="form.hora_recepcion" required />
        <input type="date" v-model="form.fecha_entrega" required />
        <input type="time" v-model="form.hora_entrega" required />
        <select v-model="form.entregado_a_id" required>
          <option disabled value="">Selecciona un usuario</option>
          <option v-for="user in usuarios" :key="user.id" :value="user.id">
            {{ user.first_name }} {{ user.last_name }}
          </option>
        </select>
        <button type="submit">Guardar</button>
      </form>
    </div>

    <!-- TABLA -->
    <table v-if="notificaciones.length">
      <thead>
        <tr>
          <th>#</th>
          <th>Entidad</th>
          <th>Expediente</th>
          <th>Dirigido a</th>
          <th>Recepcionista</th>
          <th>Recepción</th>
          <th>Entregado a</th>
          <th>Entrega</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(n, i) in notificaciones" :key="n.id">
          <td>{{ i + 1 }}</td>
          <td>{{ n.entidad_emisora }}</td>
          <td>{{ n.numero_expediente }}</td>
          <td>{{ n.dirigido_a }}</td>
          <td>{{ formatRecepcionista(n.recepcionista) }}</td>
          <td>{{ formatFechaHora(n.fecha_recepcion, n.hora_recepcion) }}</td>
          <td>{{ n.entregado_a?.first_name }} {{ n.entregado_a?.last_name }}</td>
          <td>{{ formatFechaHora(n.fecha_entrega, n.hora_entrega) }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import api from '../services/api'

export default {
  data() {
    return {
      showForm: false,
      form: {
        fecha_recepcion: '',
        hora_recepcion: '',
        entidad_emisora: '',
        numero_expediente: '',
        dirigido_a: '',
        recepcionista: '',
        fecha_entrega: '',
        hora_entrega: '',
        entregado_a_id: '',
      },
      usuarios: [],
      notificaciones: [],
    }
  },
  async mounted() {
    console.log('BASE URL EN USO:', api.defaults.baseURL)
    await this.getUsuarios()
    await this.getNotificaciones()
  },
  methods: {
    async getUsuarios() {
      try {
        const res = await api.get('/usuarios/')
        this.usuarios = res.data
      } catch (error) {
        console.error('Error al cargar usuarios:', error)
      }
    },
    async getNotificaciones() {
      try {
        const res = await api.get('/notificaciones/')
        this.notificaciones = res.data
      } catch (error) {
        console.error('Error al cargar notificaciones:', error)
      }
    },
    async submitForm() {
      try {
        const payload = {
          ...this.form,
          hora_recepcion: this.form.hora_recepcion.length === 5 ? this.form.hora_recepcion + ':00' : this.form.hora_recepcion,
          hora_entrega: this.form.hora_entrega.length === 5 ? this.form.hora_entrega + ':00' : this.form.hora_entrega,
        }

        await api.post('/notificaciones/', payload)
        alert('✅ Notificación registrada')
        this.resetForm()
        this.getNotificaciones()
        this.showForm = false
      } catch (error) {
        console.error('Error al enviar:', error.response?.data || error)
        alert('Error: ' + JSON.stringify(error.response?.data || {}))
      }
    },
    resetForm() {
      this.form = {
        fecha_recepcion: '',
        hora_recepcion: '',
        entidad_emisora: '',
        numero_expediente: '',
        dirigido_a: '',
        recepcionista: '',
        fecha_entrega: '',
        hora_entrega: '',
        entregado_a_id: '',
      }
    },
    formatFechaHora(f, h) {
      return f && h ? `${f} ${h.slice(0, 5)}` : ''
    },
    formatRecepcionista(code) {
      const nombres = {
        amanda: 'Amanda González',
        wanda: 'Wanda Pastor'
      }
      return nombres[code] || code
    }
  }
}
</script>
