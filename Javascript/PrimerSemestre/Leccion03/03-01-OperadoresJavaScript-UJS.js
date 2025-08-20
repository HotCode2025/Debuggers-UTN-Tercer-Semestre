
// Ejercicio para encontrar números pares
let numero = 8;

if (numero % 2 == 0){
    console.log("Es un número PAR");
}
else{
    console.log("Es un número IMPAR");
}

// Ejercicio: es mayor de edad
var edad = 18;
if( edad >= 18){
    console.log("Es mayor de edad");
}
else{
    console.log("Es menor de edad");
}

//Ejercicio: Dentro de un rango
let dentroRago = 10; //Aqui vamos a ir cambiando el valor
let valMin = 0; valMax = 10;
if( dentroRago >= valMin && dentroRago <= valMax){
    console.log("Esta dentro del rango establecido")
}
else{
    console.log("Esta fuera del rango establecido")
}

// Ejercicio: Si el padre puede asistir al juego de su hijo
let vacaciones = true;
let diaDescanso = false;
if(vacaciones || diaDescanso){
    console.log("El padre puede asistir al juego de su hijo")
}
else{
    console.log("El padre No puede asistir al juego de su hijo")
}

//Operador ternario
let resultado2 = 3 > 2 ? "Verdadero" : "Falso";
console.log(resultado2)
let numero1 = 12;
resultado2 = numero1 % 2 == 0 ? "Es un numero PAR" : "Es un numero IMPAR";
console.log(resultado2)

//Convertir String a Number
let miNumero = "21";//Es una cadena
console.log(typeof miNumero);
let edad2 = Number(miNumero);//Esta es una funcion
console.log(typeof edad2);
//Funcion isNan
if(isNaN(edad2)){ //No es un numero = is Not a Number(devuelve un resultado booleano)
    console.log("Esta variable no contiene solo numeros")
}
else{
    if(edad2 >= 18){
        console.log("Puede votar");
    }
    else{
        console.log("Muy joven para votar");
    }
}

//Operador ternario
let resultado3 = edad2 >= 18 ? "Puede votar" : "Muy joven para votar";
console.log(resultado3);
