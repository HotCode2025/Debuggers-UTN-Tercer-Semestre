'use strict';

let x = 10;



//Veremos como evitar el error
try {
    let x = 10; 
    miFuncion();

}
catch (error) { //catchamos el error
    console.log('Se ha producido un error: ' + error);
}
finally {
    console.log('Termina la revision de errores'); //Esto se ejecuta siempre, haya o no error
}


console.log('Continuamos... '); //Esto no se llega a ver porque esta bloqueado (Roto)
