
import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000/api', // Ajustar segun nuestro backend
  timeout: 10000, // Tiempo de espera de 10 segundos
})

export default api
