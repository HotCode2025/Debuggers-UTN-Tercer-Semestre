"use strict"; //Modo estricto, no permite declarar variables sin var, let o const

x = 10; //la variable x no ha sido declarada, por lo que se lanza un error en modo estricto
console.log(x);

var x = 10; //la variable x ha sido declarada, por lo que no se lanza un error en modo estricto
console.log(x);


miFuncion(); //la función miFuncion no ha sido declarada, por lo que se lanza un error en modo estricto


function miFuncion() {
   y = 10; //la variable y no ha sido declarada, por lo que se lanza un error en modo estricto
   var y = 13; //la variable y ha sido declarada, por lo que no se lanza un error en modo estricto
   console.log(y);
}

//el use strict no entra en funciones flecha, por lo que no se lanza un error en modo estricto.

