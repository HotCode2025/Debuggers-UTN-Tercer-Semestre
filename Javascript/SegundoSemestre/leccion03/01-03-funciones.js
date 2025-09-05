//1.1 Introduccion a Funciones

miFuncion(8, 2); //Esto se le conoce como hosting
function miFuncion(a, b){
    console.log("Sumamos: "+ (a + b));
}

//Llamando la funcion
miFuncion(5, 4);

// 1.2 Palabra return

miFuncion(8, 2); //Esto se le conoce como hosting
function miFuncion(a, b){
    return a + b;
}

let resultado = miFuncion(6, 7);
console.log(resultado);

// 1.3 Funciones de tipo expresión

// Declaramos una función de tipo expresión
let x = function(a, b){ return a + b}; //necesita cierre con punto y coma
resultado = x(5, 6); //al llamarla se pone la variable y parentesis
console.log(resultado);

// 1.4 Funciones de tipo self y invoking
(function(a, b){
    console.log('Ejecutando la función: '+ (a + b));
})(9, 6);

// 1.5 Tipos de datos en una función

console.log(typeof miFuncion);
function miFuncionDos(a, b){
    console.log(arguments.length);
}

miFuncionDos(5, 7);

// toString
var miFuncionTexto = miFuncionDos.toString();// convierte la funcion a texto
console.log(miFuncionTexto);

// 1.6 Funciones flecha
const sumarFuncionFlecha = (a, b) => a + b;
resultado = sumarFuncionFlecha(3, 7); // Asignamos el valor a una variable
console.log(resultado);

// 1.7 Argumentos y parametros
// Funcion tipo expresion
let sumar = function(a = 4,b = 8){
    console.log(arguments[0]); //muestra el parametro de: a
    console.log(arguments[1]); //muestra el parametro de: b
    return a + b + arguments[2];
}
resultado = sumar(3, 2, 9);
console.log(resultado);

// 1.8 Concepto hoisting
// Sumar todos los argumentos
let respuesta = sumarTodo(5, 4, 13, 10, 9);
console.log(respuesta);
function sumarTodo(){
    let suma = 0;
    for(let i = 0; i < arguments.length; i++){
        suma += arguments[i]; // Arguments es para arreglos
    }
    return suma;
}

// 1.9 Paso por valor
// Tipos primitivos
let k = 10;
function cambiarValor(a){ // Paso por valor
    a = 20;
}

cambiarValor(k);
console.log(k)

// 1.9.1 Paso por referencia
const persona = {
    nombre: 'Juan',
    apellido: 'Lepez'
}
console.log(persona);
function cambiarValorObjeto(p1){
    p1.nombre = 'Ignacio';
    p1.apellido = 'Perez';
}

cambiarValorObjeto(persona);
console.log(persona);









