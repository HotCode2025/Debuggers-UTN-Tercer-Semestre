// 6.1 Sintaxis de clases en JavaScript: Parte 1 y 2

class Persona{ //Clase padre

    static contadorPersonas = 0; // Atributo estático  8.2 Atributos estáticos
    //email = 'Valor default email';// Atributo no estatico   8.3 Atributos estáticos vs No estáticos

    static get MAX_OBJ(){ // Este método simula una constante   8.5 Creación de constantes estáticas
        return 5;
    }

    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
        if(Persona.contadorPersonas < Persona.MAX_OBJ){
             this.idPersona = ++Persona.contadorPersonas; //8.4 Uso de la palabra static: Parte 1 y 2
       // console.log('Se incrementa el contador: '+Persona.contadorObjetosPersona);
        }
        else{
            console.log('Se ha superado el máximo de objetos permitidos');
        }
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

// Clase 7 , 7.1 Heredar métodos
    nombreCompleto(){
        return this.idPersona+' '+this._nombre+' '+this._apellido;// 8.4 Uso de la palabra static: Parte 1 y 2
    }

//7.3 Clase Object, toString, sobreescritura y Polimorfismo
// Sobreescribiendo el método de la clase padre (Object)
    toString(){ // Regresa un String
        // Se aplica el polimorfismo que significa = multiples formas en tiempo de ejecución
        // El método que se ejecuta depende si es una referencia de tipo padre o hija
        return this.nombreCompleto();
    }

// 8.1 Palabra static con métodos: Parte 1 y 2
    static saludar(){
        console.log('Saludos desde este método static');
    }

    static saludar2(persona){
        console.log(persona.nombre+' '+persona.apellido);
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

// 7.2 Sobreescritura
// Sobreescritura
    nombreCompleto(){
        return super.nombreCompleto()+', '+this._departamento;
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
console.log(empleado1.nombreCompleto());

//Object.prototype.toString // Esta es la manera de acceder a atributos y métodos de manera dinamica
//7.3 Clase Object, toString, sobreescritura y Polimorfismo
console.log(empleado1.toString());
console.log(persona1.toString());
// 8.1 Palabra static con métodos: Parte 1 y 2
// persona1.saludar(); no se utiliza desde el objeto
Persona.saludar();
Persona.saludar2(persona1);

Empleado.saludar();
Empleado.saludar2(empleado1);

//8.2 Atributos estáticos
//console.log(persona1.contadorObjetosPersona);
console.log(Persona.contadorObjetosPersona);
console.log(Empleado.contadorObjetosPersona);

// 8.3 Atributos estáticos vs No estáticos
//console.log(Persona.email);No se puede acceder desde la clase
console.log(persona1.email);
console.log(empleado1.email);

//8.4 Uso de la palabra static: Parte 1 y 2
console.log(persona1.toString());
console.log(persona2.toString());
console.log(empleado1.toString());
console.log(Persona.contadorPersonas);
let persona3 = new Persona('Pablo', 'Lopez');
console.log(persona3.toString());
console.log(Persona.contadorPersonas);

// 8.5 Creación de constantes estáticas
console.log(Persona.MAX_OBJ);
//Persona.MAX_OBJ = 10; // No se puede modificar, ni alterar
console.log(Persona.MAX_OBJ);

let persona4 = new Persona('Franco', 'Diaz');
console.log(persona4.toString());
let persona5 = new Persona('Tito', 'Paz');
console.log(persona5.toString());
