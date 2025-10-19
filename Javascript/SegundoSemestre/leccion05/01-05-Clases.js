// 6.1 Sintaxis de clases en JavaScript: Parte 1 y 2

class Persona{ //Clase padre
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }

    get nombre(){
        return this._nombre
    }

    get apellido(){
        return this._apellido
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    set apellido(apellido){
        this._apellido = apellido
    }
}

class Empleado extends Persona{ // Clase hija
    constructor(nombre, apellido, departamento){
        super(nombre, apellido)
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }

    set departamento(departamento){
        this._departamento = departamento;
    }
}

let persona1 = new Persona('Martin', 'Perez');
console.log(persona1);
let persona2 = new Persona('Carlos', 'Lara');
console.log(persona2);

// 6.2 Método Get y Set: Parte Get y Parte Set
// Parte Get
console.log(persona1.nombre);
console.log(persona1.apellido);
console.log(persona2.nombre);
console.log(persona2.apellido);

// Parte set
persona1.apellido = 'Caras';
console.log(persona1.apellido);
persona2.nombre = 'Maria Laura';
console.log(persona2.nombre);
persona2.apellido = 'Moreno';
console.log(persona2.apellido);

// 6.3 Hoisting y Clases: Parte 1 y 2
// No se puede crear un objeto antes de la clase 

// 6.4 Herencia: Parte 1 y 2

let empleado1 = new Empleado('Maria', 'Gimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1._nombre)



