var nombre = "Jose ";
var apellido = "Montes";
var nombreCompleto = nombre+" "+apellido; //Primera concanetación
console.log(nombreCompleto);
var nombreCompleto2 = "Jairo"+" "+"Ubilla";//Segunda concatenación
console.log(nombreCompleto2)
var juntos = nombre + 219;//Lee de izq a der siguiendo la cadena, le el numero como str
console.log(juntos);
juntos = nombre + 78 + 17;//Aqui se puede diferenciar a traves de los parentesis
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido;//Tercera concatenacion usando el operador simplificado
console.log(nombre);

//Hoy ya no se usa var, se utiliza let y const
let nombre2 = "Pedro";
console.log(nombre2);

const apellido2 = "Lepes";
//Apellido2 = "peres";una constante no puede ser modificada
console.log(apellido2);

let x, y;//Se pueden crear varias variables dentro de una misma linea
x = 17, y = 21;//Se puede hacer asignacion de varias variables dentro de una misma linea
let z = x + y;//Se asigna el valor de la operacion
console.log(z);

let _1num = 31; //No utilizar numeros para iniciar el nombre de una variable
let rompiendo = "rompe";//No utilizar palabras reservadas para variables

console.log(_1num);
console.log(rompiendo);

//Ampliando el uso de var let y const

/*
Con var puedes reasignar en cualquier momento
este forma parte del ambito global
Un error es que se sobreescriba
*/

var nombre = "Ariel";
nombre = "Osvaldo";
console.log(nombre);

function saludar(){
    var nombre3 = "Natalia";
    console.log(nombre3);
}
//console.log(nombre3);//Aqui no lee el dato de la funcion

if(true){
    var edad = 34;
    console.log(edad);
}
console.log(edad);//En la funcion funciono correctamete, en le estructura if fallo

/*
let: esta puede ser reasignada en cualquier momento 
la diferencia es que su ambito es de bloque,
solo disponible dentro de un bloque de llaves 
o dentro de una funcion
*/ 

function saludar(){
    let nombre2 = "Ariel";
    console.log(nombre2);
}
//console.log(nombre2);

if(true){
    let edad2 = 33;
    console.log(edad2);
}
//console.log(edad2);

/*
const se utiliza para valores constantes que no pueden ser reasignados
*/

const fechaNacimiento = 2006;
console.log(fechaNacimiento);
//fechaNacimiento = 2003;
//console.log(fechaNacimiento);//Solo se ejecuta el console anterior



