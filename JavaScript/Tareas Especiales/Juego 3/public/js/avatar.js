function iniciarJuego() {
    let botonPersonajeJugador = document.getElementById('boton-personaje');
    botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);
}

function seleccionarPersonajeJugador() {
    let personajeSeleccionado = "";
    let spanPersonajeJugador = document.getElementById('personaje-jugador');

    // uso de condicionales if-else 
    if (document.getElementById('zuko').checked) {
        personajeSeleccionado = "Zuko";
    } else if (document.getElementById('katara').checked) {
        personajeSeleccionado = "Katara";
    } else if (document.getElementById('aang').checked) {
        personajeSeleccionado = "Aang";
    } else if (document.getElementById('toph').checked) {
        personajeSeleccionado = "Toph";
    }

    // uso de bucle for
    let opcionesPersonajes = document.getElementsByName('personaje');
    for (let i = 0; i < opcionesPersonajes.length; i++) {
        if (opcionesPersonajes[i].checked) {
            personajeSeleccionado = opcionesPersonajes[i].id;
            break; 
        }
    }

    // muestro el personaje seleccionado
    if (personajeSeleccionado !== "") {
        //alert('SELECCIONASTE TU PERSONAJE: ' + personajeSeleccionado.toUpperCase());
        spanPersonajeJugador.innerHTML = personajeSeleccionado.toUpperCase();

        seleccionarPersonajeEnemigo(personajeSeleccionado);

    } else {
        alert('POR FAVOR, SELECCIONA UN PERSONAJE ANTES DE CONTINUAR.');
    }
}

function seleccionarPersonajeEnemigo(personajeJugador) {
    let spanPersonajeEnemigo = document.getElementById('personaje-enemigo');
    let personajeEnemigo = "";

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

window.addEventListener('load', iniciarJuego);