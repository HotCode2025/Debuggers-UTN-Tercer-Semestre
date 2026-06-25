// Estado compartido del usuario autenticado y del turno en construcción.
import { defineStore } from 'pinia'

const turnoVacio = () => ({
  establecimiento: null,
  especialidad: null,
  profesional: null,
  fecha: '',
  hora: ''
})

// Las funciones fábrica evitan reutilizar referencias entre limpiezas de estado.
const usuarioVacio = () => ({
  nombre: '',
  dni: '',
  email: '',
  tel: '',
  rol: ''
})

const obtenerUsuarioGuardado = () => {
  // Recupera la sesión visual al recargar sin reemplazar la seguridad del backend.
  try {
    return JSON.parse(localStorage.getItem('usuario')) || usuarioVacio()
  } catch {
    localStorage.removeItem('usuario')
    return usuarioVacio()
  }
}

export const useTurnosStore = defineStore('turnos', {
  state: () => ({
    usuario: obtenerUsuarioGuardado(),
    turnoProceso: turnoVacio(),
    turnosConfirmados: []
  }),
  actions: {
    confirmarTurnoActual() {
      // Conserva un resumen local inmediato; la fuente definitiva permanece en Django.
      this.turnosConfirmados.push({
        id: Date.now(),
        ...this.turnoProceso,
        paciente: this.usuario
      })

      this.limpiarTurnoProceso()
    },
    limpiarTurnoProceso() {
      this.turnoProceso = turnoVacio()
    },
    cerrarSesion() {
      // Elimina estado de navegación y credenciales persistidas en una sola acción.
      this.usuario = usuarioVacio()
      this.limpiarTurnoProceso()
      this.turnosConfirmados = []
      localStorage.removeItem('access')
      localStorage.removeItem('refresh')
      localStorage.removeItem('usuario')
    }
  }
})
