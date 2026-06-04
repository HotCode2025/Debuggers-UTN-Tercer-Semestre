const TAMANIO = 8;

// Los 8 desplazamientos posibles del caballo 
// d = {(2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1)}
const MOVIMIENTOS = [
  [2, 1], [1, 2], [-1, 2], [-2, 1],
  [-2, -1], [-1, -2], [1, -2], [2, -1]
];

let recorrido = [];
let temporizadorAnimacion = null;
let pasoActual = 0;
let animando = false;

// Tablero vacio en pantalla
function construirTablero() {
  const tablero = document.getElementById('tablero');
  tablero.innerHTML = '';
  for (let fila = 0; fila < TAMANIO; fila++) {
    for (let columna = 0; columna < TAMANIO; columna++) {
      const casilla = document.createElement('div');
      casilla.className = 'casilla';
      casilla.id = 'casilla_' + fila + '_' + columna;
      casilla.innerHTML =
        '<span id="num_' + fila + '_' + columna + '"></span>' +
        '<span class="coordenada">' + columna + ',' + (TAMANIO - 1 - fila) + '</span>';
      tablero.appendChild(casilla);
    }
  }
}

// Verifica si la casilla (x, y) esta dentro del tablero y no fue visitada
function esMovimientoValido(tablero, x, y) {
  return x >= 0 && y >= 0 &&
         x < TAMANIO && y < TAMANIO &&
         tablero[y][x] === 0;
}

// Algoritmo de vuelta atras (backtracking)
// Prueba los 8 movimientos en orden. Si ninguno funciona, borra y retrocede.
function backtracking(tablero, x, y, numeroSalto, camino) {
  // Condicion de exito: se realizaron n*n - 1 saltos (63 saltos = 64 casillas)
  if (numeroSalto === TAMANIO * TAMANIO) return true;

  // Probar cada uno de los 8 movimientos posibles
  for (let i = 0; i < MOVIMIENTOS.length; i++) {
    const nx = x + MOVIMIENTOS[i][0];
    const ny = y + MOVIMIENTOS[i][1];

    if (esMovimientoValido(tablero, nx, ny)) {
      // Anotar el salto en la casilla destino
      tablero[ny][nx] = numeroSalto + 1;
      camino.push({ x: nx, y: ny, paso: numeroSalto + 1 });

      // Llamada recursiva con la nueva posicion
      if (backtracking(tablero, nx, ny, numeroSalto + 1, camino)) {
        return true; // solucion encontrada
      }

      // Vuelta atras: borrar la anotacion y ensayar con el siguiente movimiento
      tablero[ny][nx] = 0;
      camino.pop();
    }
  }

  return false; // ningun movimiento llevo a la solucion
}

function iniciarRecorrido() {
  reiniciarTablero();
  actualizarEstado('Calculando... (puede tardar unos segundos)');
  document.getElementById('botonResolver').disabled = true;

  setTimeout(function() {
    // Tablero inicializado en 0 = ninguna casilla visitada
    const tablero = Array.from({ length: TAMANIO }, () => Array(TAMANIO).fill(0));
    const camino = [];

    // El caballo arranca en la posicion (0, 0) — esquina inferior izquierda
    const inicioX = 0;
    const inicioY = 0;

    tablero[inicioY][inicioX] = 1;
    camino.push({ x: inicioX, y: inicioY, paso: 1 });

    const encontrado = backtracking(tablero, inicioX, inicioY, 1, camino);

    if (!encontrado) {
      actualizarEstado('No se encontro solucion desde (0, 0).');
      document.getElementById('botonResolver').disabled = false;
      return;
    }

    recorrido = camino;
    actualizarEstado('Solucion encontrada. Presiona Animar para verla.');
    document.getElementById('botonAnimar').disabled = false;
  }, 50);
}

function alternarAnimacion() {
  if (animando) {
    pausarAnimacion();
  } else {
    reproducirAnimacion();
  }
}

function reproducirAnimacion() {
  animando = true;
  document.getElementById('botonAnimar').textContent = 'Pausar';
  animarRecorrido();
}

function pausarAnimacion() {
  animando = false;
  clearTimeout(temporizadorAnimacion);
  document.getElementById('botonAnimar').textContent = 'Animar';
}

function animarRecorrido() {
  if (pasoActual >= recorrido.length) {
    animando = false;
    document.getElementById('botonAnimar').textContent = 'Animar';
    document.getElementById('botonAnimar').disabled = true;
    actualizarEstado('Recorrido completo. Se visitaron las 64 casillas.');
    return;
  }

  const { x, y, paso } = recorrido[pasoActual];
  const fila = TAMANIO - 1 - y;

  // Marcar la casilla anterior como visitada
  if (pasoActual > 0) {
    const anterior = recorrido[pasoActual - 1];
    const filaAnterior = TAMANIO - 1 - anterior.y;
    const casillaAnterior = document.getElementById('casilla_' + filaAnterior + '_' + anterior.x);
    casillaAnterior.className = 'casilla visitada';
  }

  // Marcar la casilla actual
  const casillaActual = document.getElementById('casilla_' + fila + '_' + x);
  casillaActual.className = 'casilla ' + (paso === 1 ? 'origen' : 'actual');
  document.getElementById('num_' + fila + '_' + x).textContent = paso;

  actualizarEstado('Salto ' + paso + ' / 64  —  posicion (' + x + ', ' + y + ')');

  pasoActual++;
  const demora = 630 - parseInt(document.getElementById('velocidad').value);
  temporizadorAnimacion = setTimeout(animarRecorrido, Math.max(30, demora));
}

function reiniciarTablero() {
  clearTimeout(temporizadorAnimacion);
  animando = false;
  pasoActual = 0;
  recorrido = [];
  construirTablero();
  actualizarEstado('');
  document.getElementById('botonAnimar').disabled = true;
  document.getElementById('botonAnimar').textContent = 'Animar';
  document.getElementById('botonResolver').disabled = false;
}

function actualizarEstado(mensaje) {
  document.getElementById('estado').textContent = mensaje;
}

construirTablero();
