<template>
  <div class="container mt-5">
    <h2 class="text-center mb-4">📋 Notificaciones</h2>

    <!-- BOTÓN PARA ABRIR MODAL -->
    <div class="text-center mb-4">
      <button class="btn btn-success" data-bs-toggle="modal" data-bs-target="#modalForm">
        📩 Registrar Nueva Notificación
      </button>
    </div>

    <!-- MODAL DEL FORMULARIO -->
    <div class="modal fade" id="modalForm" tabindex="-1" aria-labelledby="modalFormLabel" aria-hidden="true">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <form @submit.prevent="submitForm">
            <div class="modal-header">
              <h5 class="modal-title">📄 Formulario de Notificación</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Cerrar"></button>
            </div>
            <div class="modal-body">
              <div class="row g-3">
                <div class="col-md-6">
                  <label class="form-label">Fecha de recepción</label>
                  <input type="date" class="form-control" v-model="form.fecha_recepcion" required />
                </div>
                <div class="col-md-6">
                  <label class="form-label">Hora de recepción</label>
                  <input type="time" class="form-control" v-model="form.hora_recepcion" required />
                </div>
                <div class="col-md-6">
                  <label class="form-label">Entidad emisora</label>
                  <input type="text" class="form-control" v-model="form.entidad_emisora" required />
                </div>
                <div class="col-md-6">
                  <label class="form-label">Número de expediente</label>
                  <input type="text" class="form-control" v-model="form.numero_expediente" required />
                </div>
                <div class="col-md-6">
                  <label class="form-label">Dirigido a</label>
                  <input type="text" class="form-control" v-model="form.dirigido_a" required />
                </div>
                <div class="col-md-6">
                  <label class="form-label">Recepcionista</label>
                  <select class="form-select" v-model="form.recepcionista" required>
                    <option disabled value="">Selecciona un recepcionista</option>
                    <option value="amanda">Amanda González</option>
                    <option value="wanda">Wanda Pastor</option>
                  </select>
                </div>
                <div class="col-md-6">
                  <label class="form-label">Fecha de entrega</label>
                  <input type="date" class="form-control" v-model="form.fecha_entrega" required />
                </div>
                <div class="col-md-6">
                  <label class="form-label">Hora de entrega</label>
                  <input type="time" class="form-control" v-model="form.hora_entrega" required />
                </div>
                <div class="col-12">
                  <label class="form-label">Entregado a</label>
                  <select class="form-select" v-model="form.entregado_a_id" required>
                    <option disabled value="">Selecciona un usuario</option>
                    <option v-for="user in usuarios" :key="user.id" :value="user.id">
                      {{ user.first_name }} {{ user.last_name }}
                    </option>
                  </select>
                </div>
              </div>
            </div>
            <div class="modal-footer">
              <button type="submit" class="btn btn-primary">Guardar Notificación</button>
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
            </div>
          </form>
        </div>
      </div>
    </div>

    <!-- TABLA DE NOTIFICACIONES -->
    <div class="mt-5">
      <h4 class="text-center mb-3">📋 Lista de Notificaciones</h4>
      <div v-if="notificaciones.length === 0" class="alert alert-info text-center">
        No hay notificaciones registradas.
      </div>
      <div v-else class="table-responsive">
        <table class="table table-bordered table-hover">
          <thead class="table-dark">
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
    </div>
  </div>
</template>

<script>
import api from '../services/api'

export default {
  name: 'NotificationModalForm',
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
        entregado_a_id: '',
      },
      usuarios: [],
      notificaciones: []
    }
  },
  async mounted() {
    console.log('BASE URL en uso:', api.defaults.baseURL)
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
          hora_entrega: this.form.hora_entrega.length === 5 ? this.form.hora_entrega + ':00' : this.form.hora_entrega
        }

        await api.post('/notificaciones/', payload)
        alert('✅ Notificación registrada')
        this.resetForm()
        this.getNotificaciones()
        document.querySelector('#modalForm .btn-close').click()
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
