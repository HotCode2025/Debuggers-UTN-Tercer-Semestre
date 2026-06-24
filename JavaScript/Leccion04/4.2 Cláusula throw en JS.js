'use strict'
//Veamos como evitar esta error
try {
    let x = 10; //Lo traemos con alt + flecha hacia arriba o hacia abajo
    //miFuncion(); //Capturamos el error de la funcion
    throw'Mi Error';//Maneja tipo String
}
catch (error){ //Catchamos el error
    console.log( typeof(error) );
}
finally {
    console.log('Termina la recision de errores');
}
//La ejecucion ahora continua...
console.log('Continuamos...')

let resultado = 'hola';

try {
    //y = 5;
    if( isNaN(resultado)) throw 'No es un número';
    else if( resultado === '') throw'es cadena vacia';
    else if( resultado >=0)throw'valor positivo';
    else if( resultado <=0)throw'valor negativo';
}
catch(error) {
    console.log(error);
    console.log(error.name);
    console.log(error.message);
}
finally {
    console.log('Termina la revision de errores');
}