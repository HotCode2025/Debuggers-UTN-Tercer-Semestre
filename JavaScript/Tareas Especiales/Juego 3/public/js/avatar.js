let ataqueJugador; // ataque del jugador
let ataqueEnemigo; // ataque de la computadora
let vidasJugador = 3; // vidas del jugador
let vidasEnemigo = 3; // vidas del enemigo

function iniciarJuego() {
    let botonPersonajeJugador = document.getElementById('boton-personaje');
    botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);

    let botonPunio = document.getElementById('boton-punio');
    botonPunio.addEventListener('click', ataquePunio);
    let botonPatada = document.getElementById('boton-patada');
    botonPatada.addEventListener('click', ataquePatada);
    let botonBarrida = document.getElementById('boton-barrida');
    botonBarrida.addEventListener('click', ataqueBarrida);

    let botonReiniciar = document.getElementById('boton-reiniciar');
    botonReiniciar.addEventListener('click', reiniciarJuego);

    // popup con las reglas
    let popupReglas = document.getElementById('popup-reglas');
    let botonReglas = document.getElementById('boton-reglas');
    let botonCerrarReglas = document.getElementById('boton-cerrar-reglas');

    // Abre el popup
    botonReglas.addEventListener('click', () => {
        popupReglas.showModal(); 
    });

    // Cierra el popup
    botonCerrarReglas.addEventListener('click', () => {
        popupReglas.close();
    });
}

function seleccionarPersonajeJugador() {
    let personajeSeleccionado = "";
    let spanPersonajeJugador = document.getElementById('personaje-jugador');

    // Opcion 1 y Opcion 2 hacen lo mismo
    // Opcion 1 
    // uso de bucle for
    let opcionesPersonajes = document.getElementsByName('personaje');
    for (let i = 0; i < opcionesPersonajes.length; i++) {
        if (opcionesPersonajes[i].checked) {
            personajeSeleccionado = opcionesPersonajes[i].id;
            break; 
        }
    }

    // Opcion 2
    // uso de condicionales if-else 
/*
    if (document.getElementById('zuko').checked) {
        personajeSeleccionado = "Zuko";
    } else if (document.getElementById('katara').checked) {
        personajeSeleccionado = "Katara";
    } else if (document.getElementById('aang').checked) {
        personajeSeleccionado = "Aang";
    } else if (document.getElementById('toph').checked) {
        personajeSeleccionado = "Toph";
    }
*/

    // muestro el personaje seleccionado
    if (personajeSeleccionado !== "") {
        spanPersonajeJugador.innerHTML = personajeSeleccionado.toUpperCase();

        seleccionarPersonajeEnemigo(personajeSeleccionado);
    } else {
        alert('POR FAVOR, SELECCIONA UN PERSONAJE ANTES DE CONTINUAR.');
    }
}

function seleccionarPersonajeEnemigo(personajeJugador) {
    let spanPersonajeEnemigo = document.getElementById('personaje-enemigo');
    let personajeEnemigo = "";

    // Si el personaje elejido es igual al nuestro vuelve repetir el codigo
    do {
        let numeroAleatorio = Math.floor(Math.random() * (4 - 1 + 1) + 1);

        if (numeroAleatorio === 1) {
            personajeEnemigo = "zuko";
        } else if (numeroAleatorio === 2) {
            personajeEnemigo = "katara";
        } else if (numeroAleatorio === 3) {
            personajeEnemigo = "aang";
        } else if (numeroAleatorio === 4) {
            personajeEnemigo = "toph";
        }
    } while (personajeEnemigo == personajeJugador);

    spanPersonajeEnemigo.innerHTML = personajeEnemigo.toUpperCase();
}

// Al presionar cada botón selecionamos el ataque y llamamos la funcion del combate
function ataquePunio() {
    ataqueJugador = 'Puño';
    funcionCombate();
}

function ataquePatada() {
    ataqueJugador = 'Patada';
    funcionCombate();
}

function ataqueBarrida() {
    ataqueJugador = 'Barrida';
    funcionCombate();
}

function funcionCombate() {
    // Verificamos que se haya elejido un personaje antes de comenzar la batalla
    let personajeJugador = document.getElementById('personaje-jugador').innerHTML;
    if (!personajeJugador) {
        alert('Primero debes seleccionar un personaje.');
        return;
    }

    ataqueAleatorioEnemigo();
    combate();
}

// ----------------------------------------------------------------------------------------------------------
// Agragamos la logica de la batalla
function combate() {
    let spanVidasJugador = document.getElementById('vidas-jugador');
    let spanVidasEnemigo = document.getElementById('vidas-enemigo');
    let sectionMensajes = document.getElementById('mensajes');
    let resultadoRound = "";

    // Caso de Empate
    if (ataqueJugador === ataqueEnemigo) {
        resultadoRound = "EMPATE 🤝";
    } 
    // Casos donde GANA el Jugador
    else if ((ataqueJugador === 'Patada' && ataqueEnemigo === 'Puño') ||
        (ataqueJugador === 'Puño' && ataqueEnemigo === 'Barrida') ||
        (ataqueJugador === 'Barrida' && ataqueEnemigo === 'Patada')) {
            resultadoRound = "GANASTE EL ROUND 🎉";
            vidasEnemigo--; // Restamos vida al enemigo
            spanVidasEnemigo.innerHTML = vidasEnemigo; 
    } 
    // Si no es empate ni gano el jugador, gano el enemigo
    else {
        resultadoRound = "PERDISTE EL ROUND ❌";
        vidasJugador--; // Restamos vida al jugador
        spanVidasJugador.innerHTML = vidasJugador; 
    }

    // Mostramos que ataque elejimos nosotros y que elejio la maquina
    sectionMensajes.innerHTML = `<p>Tu personaje atacó con <strong>${ataqueJugador}</strong>, el enemigo atacó con <strong>${ataqueEnemigo}</strong> - <strong>${resultadoRound}</strong></p>`;

    // Chequeamos si aun los jugadores tienen vidas
    revisarVidas();
}

function revisarVidas() {
    if (vidasJugador === 0) {
        finalizarJuego("El enemigo te ha derrotado... 😢");
    } else if (vidasEnemigo === 0) {
        finalizarJuego("¡Felicidades! Has ganado 🏆");
    }
}

function finalizarJuego(mensajeFinal) {
    let sectionMensajes = document.getElementById('mensajes');
    sectionMensajes.innerHTML = `<p style="font-size: 1.2em; color: red;"><strong>${mensajeFinal}</strong></p>`;

    // Deshabilitamos los botones para que no puedan seguir jugando tras terminar
    document.getElementById('boton-punio').disabled = true;
    document.getElementById('boton-patada').disabled = true;
    document.getElementById('boton-barrida').disabled = true;
}

function reiniciarJuego() {
    location.reload();
}
// -------------------------------------------------------------------------------------------------------

function ataqueAleatorioEnemigo() {
    let ataqueAleatorio = aleatorio(1, 3);

    if (ataqueAleatorio == 1) {
        ataqueEnemigo = 'Puño';
    } else if (ataqueAleatorio == 2) {
        ataqueEnemigo = 'Patada';
    } else {
        ataqueEnemigo = 'Barrida';
    }
}

function aleatorio(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}

window.addEventListener('load', iniciarJuego);