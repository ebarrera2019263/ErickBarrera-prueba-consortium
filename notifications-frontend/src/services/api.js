import axios from 'axios'

const api = axios.create({
  baseURL: 'https://erickbarrera-prueba-consortium.onrender.com', // tu backend en Render
  timeout: 10000,
})

export default api
