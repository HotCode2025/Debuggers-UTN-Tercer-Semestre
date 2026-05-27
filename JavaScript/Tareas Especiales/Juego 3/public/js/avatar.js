function seleccionarPersonajeJugador() {
    let opcionesPersonajes = document.getElementsByName('personaje');
    let personajeSeleccionado = "";

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
    for (let i = 0; i < opcionesPersonajes.length; i++) {
        if (opcionesPersonajes[i].checked) {
            personajeSeleccionado = opcionesPersonajes[i].id;
            break; 
        }
    }

    // muestro el personaje seleccionado
    if (personajeSeleccionado !== "") {
        alert('SELECCIONASTE TU PERSONAJE: ' + personajeSeleccionado.toUpperCase());
    } else {
        alert('POR FAVOR, SELECCIONA UN PERSONAJE ANTES DE CONTINUAR.');
    }
}

let botonPersonajeJugador = document.getElementById('boton-personaje');
botonPersonajeJugador.addEventListener('click', seleccionarPersonajeJugador);
