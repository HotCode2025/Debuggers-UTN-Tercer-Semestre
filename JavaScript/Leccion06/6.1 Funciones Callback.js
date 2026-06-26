miFuncion1()
miFuncion2()
function miFuncion1(){
    console.log('Funcion 1');
}

function miFuncion2(){
    console.log('Función 2');
}


//Funcion de tipo callback

function imprimir(mensaje){
    console.log(mensaje);
}

function sumar(op1,op2,funcionCallback){
    let res = op1 + op2;
    funcionCallback(`resultado: ${res}`);
}

sumar(5,3,imprimir);


