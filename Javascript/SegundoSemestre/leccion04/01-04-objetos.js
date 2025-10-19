// Introduccion a los Objetos en JavaScript Parte 1 y 2

let x = 10; //Variable de tipo primitiva
console.log(x.length); 
console.log('Tipos primitivos');

// Objeto
let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad: 30
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);

// 1.2 Agregamos métodos a los Objetos
let persona1 = {
    nombre: 'Pedro',
    apellido: 'Garcia',
    email: 'pgarcia@gmail.com',
    edad: 30,
    nombreCompleto: function(){ //método o función en JavaScript
        return this.nombre+' '+this.apellido;
    }
}
console.log(persona1.nombre);
console.log(persona1.apellido);
console.log(persona1.email);
console.log(persona1.edad);
console.log(persona1);
console.log(persona1.nombreCompleto());
console.log('Ejecutando con un objeto');

// 1.3 Diferentes formas de crear un Objeta
let persona2 = new Object(); //Debe crear un nuevo objeto en memoria
persona2.nombre = 'Juan';
persona2.direccion = 'Salada 14';
persona2.telefono = '5492618282821';
console.log(persona2.telefono);
console.log('Creamos un nuevo objeto');

// 1.4 Cómo acceder a las propiedads de los Objetos

console.log(persona['apellido']);
console.log('Usamos el ciclo for in');

// for in y accedemos al objeto como si fuera un arreglo

for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}

// 1.5 Agregar y eliminar propiedades de los Objetos

console.log('Cambiamos y eliminamos un error');
persona.apellida = 'Betancud'; //Cambiamos dinamicamente un valor del objeto
delete persona.apellida; //Eliminamos el error
console.log(persona);

// 1.6 Ejecutamos desde el navegador
// 1.7 Distintas formas de imprimir un Objeto con: Object.values() y JSON.stringify()

// Numero 1: la mas sencilla: concatenar cada valor de cada propiedad

console.log('Distintas formas de imprimir un objeto: forma 1');
console.log(persona.nombre+', '+persona.apellido);

// Número 2: A través del ciclo for in
console.log('Distintas formas de imprimir un objeto: forma 2');
for(nombrePropiedad in persona2){
    console.log(persona2[nombrePropiedad]);
}

// Número 3: La función Object.values()
console.log('Distintas formas de imprimir un objeto: forma 3');
let personaArray = Object.values(persona);
console.log(personaArray);

// Número 4: Utilizaremos el método JSON.stringify
console.log('Distintas formas de imprimir un objeto: forma 4');
let personaString = JSON.stringify(persona2);
console.log(personaString)

// Clase 05
// 5.1 Métodos get y set parte 1 
let persona3 = {
    nombre: 'Pepe',
    apellido: 'Ramos',
    edad: 25,
    email: 'pepin@gmail.com',
    nombreCompleto: function(){
        return this.nombre+' '+this.apellido;
    },
    get nombreEdad(){ //Este es el método get
        return 'El nombre es: '+this.nombre+', Edad: '+this.edad;
    }
}

console.log('Comenzamos a utilizar el método get');
console.log(persona3);
console.log(persona3.nombreEdad);

// 5.1 Métodos get y set parte 2
let persona4 = {
    nombre: 'Albert',
    apellido: 'Cantarelli',
    edad: 45,
    email: 'albert@gmail.com',
    idioma: 'es',
    get lang(){
        return this.idioma.toUpperCase();
    },
    set lang(lang){
        this.idioma = lang.toUpperCase(); // Convierte las minúsculas en mayúsculas
    }
}

console.log('Comenzamos con el método get para idiomas');
persona4.lang = 'en'
console.log(persona4.lang);

// 5.2 Constructores de objetos
function persona5(nombre, apellido, email){  // constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apellido;
    }
}
let padre = new persona5('Leo', 'Lopez', 'lopezl@gmail.com');
padre.nombre = 'Luis'; // modificamos el nombre
padre.telefono = '5492618282821'; //Una propiedad exclusiva del objeto padre
console.log(padre);
console.log(padre.nombreCompleto()); //utilizamos la funcion

let madre = new persona5('Laura', 'Contrera', 'contreral@gmail.com');
console.log(madre);
console.log(madre.telefono); //La propiedad no esta definida
console.log(madre.nombreCompleto());

// 5.3 Agregar métodos al constructor del objeto

// 5.4 Distintas formas de crear objetos

// Caso objeto 1
let miObjeto = new Object(); //Esta es una opción formal
//Caso Objeto 2
let miObjeto1 = {}; //Esta opción es breve y recomendada

// Caso String 1
let miCadena1 = new String('Hola'); //Sintaxis formal
//Caso String 2
let miCadena2 = 'Hola'; //Esta es la sintaxis simplificada y recomendada

//Caso con números 1
let miNumero = new Number(1); //Es formal no recomendable
//Caso con números 2
let miNumero1 = 1; //Sintaxis recomendada

//Caso boolean 1
let miBoolean = new Boolean(false); //Formal
//Caso boolean 2
let miBoolean1 = false; //Sintaxis recomendada

//Caso Arreglos 1
let miArreglo = new Array(); //Formal
//Caso Arreglos 2
let miArreglo1 = []; //Sintaxis recomendada

//Caso function 1
let miFuncion = new function(){}; //Todo despues de new es considerado objeto
//Caso function 2
let miFuncion1 = function(){}; //Notación simplificada y recomendada

//5.5 El uso de prototype

function persona6(nombre, apellido, email){  // constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apellido;
    }
}
let padre1 = new persona5('Tito', 'Lara', 'tlara@gmail.com');
padre1.nombre = 'Tito'; // modificamos el nombre
padre1.telefono = '549345678'; //Una propiedad exclusiva del objeto padre
console.log(padre1);
console.log(padre1.nombreCompleto()); //utilizamos la funcion

let madre1 = new persona6('Laura', 'Contrera', 'contreral@gmail.com');
console.log(madre);
console.log(madre.telefono); //La propiedad no esta definida
console.log(madre.nombreCompleto());

persona6.prototype.telefono = '261838332';
console.log(padre1);
console.log(madre1.telefono);
madre1.telefono = '54900010203';
console.log(madre1.telefono);

// 5.6 El uso de call
let persona7 = {
    nombre: 'Juan',
    apellido: 'Perez',
    nombreCompleto7: function(titulo, telefono){
        return titulo+': '+this.nombre+' '+this.apellido+' '+telefono;
    }
}

let persona8 = {
    nombre: 'Carlos',
    apellido: 'Lara'
}

console.log(persona7.nombreCompleto7('Lic.', '549261435363'));
console.log(persona7.nombreCompleto7.call(persona7, 'Ing.', '549261985789'));

// 5.7 El uso de apply

let persona9 = {
    nombre: 'Juanon',
    apellido: 'Lucero',
    nombreCompleto9: function(titulo, telefono){
        return titulo+': '+this.nombre+' '+this.apellido+' '+telefono;
    }
}

let persona01 = {
    nombre: 'Kevin',
    apellido: 'Moratal'
}

let arreglo = ['Ing.', '549837456'];
console.log(persona9.nombreCompleto9.apply(persona01, arreglo));




