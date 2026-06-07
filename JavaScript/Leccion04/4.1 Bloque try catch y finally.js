'use strict';

let x = 10;

//Veremos como evitar el error
try {
    let x = 10;
    miFuncion();
    throw 'Mi error'; //Maneja tipo string
}
catch (error) { //catchamos el error
    console.log('Se ha producido un error: ' + error);
}
finally {
    console.log('Termina la revision de errores'); //Esto se ejecuta siempre, haya o no error
}


console.log('Continuamos... '); //Esto no se llega a ver porque esta bloqueado (Roto)

//
let resultado = 'hola';
try {
    //y = 5;
    if (isNaN(resultado)) throw 'no es un numero';
    else if(resultado === '') throw 'Es una cadena vacia';
    else if(resultado >= 0) throw 'Valor positivo';
    else if(resultado < 0) throw 'Valor negativo';
}
catch (error) {
    console.log(error);
    console.log(error.name);
    console.log(error.message);
}
finally {
    console.log('Fin de la revision de errores');
}