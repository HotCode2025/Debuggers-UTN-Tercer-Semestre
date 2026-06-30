// Funcion clasica
function miFuncion() {
    console.log('Saludos desde mi funcion');
}

miFuncion ();

// ----------------------------------------------------------
let myFuncion = function () {
    console.log('Saludos desde la funcion anonima');
}

// Funcion flecha

let miFuncionFlecha = () => {
    console.log('Saludos desde mi funcion Flecha');
}

miFuncionFlecha();

// Se puede hacer en una sola linea
const saludar = () => console.log('Saludos desde esta funcion flecha');
console.log(saludar);

//  otro ejemplo
const saludar2 = () => {
    return ('Saludos desde esta funcion flecha dos')
}
console.log(saludar2());

// Simplificamos la funcion anterior
const saludar3 = () => 'Saludos desde esta funcion flecha tres';
console.log(saludar3);

// Continuamos con otro ejemplo
const regresaObjeto = () => ({nomrbre: 'Juan', apellido: 'Lara'});
console.log(regresaObjeto())

// Funciones flecha que reciben parametros
const funcionParametros = (mensaje) => console.log(mensaje);
funcionParametros('Saludos desde esta funcion con parametros');

// Funcion clasica
const funcionParametrosClasica = function(mensaje) {
    console.log(mensaje);
}
funcionParametrosClasica('Saludos desde la funcion Clasica');

// Se pueden omitor los parentesis en la funcion flecha 
const funcionConParametros = mensaje => console.log(mensaje);
funcionConParametros('Otra fomra de trabajar con funcion flecha parametros');

// Funcion flecha con varios parametros
const funcionConParametros2 = (op1, op2) => {
    let resultado = op1 + op2;
    return resultado
}
console.log(funcionConParametros2(3, 5));

