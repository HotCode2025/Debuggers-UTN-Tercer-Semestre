// 1.1 Creacion de Array o arreglos
// let autos = new Array('Ferrari', 'Renault', 'BMW'); esta es la sintaxis vieja
const autos = ['Ferrari', 'Renault', 'BMW'];
console.log(autos);

// 1.2 Recorremos los elementos de un arreglo
console.log(autos[0]);
console.log(autos[2]);

for(let i = 0; i < autos.length; i++){
    console.log([i+' ; '+autos[i]]);
}

// 1.3 Modificamos los elementos del arreglo
autos[1] = 'volvo';
console.log(autos[1]);

// Agregamos nuevos valores al arreglo
autos.push('Audio'); // Agregamos el elemento al final del arreglo
console.log(autos);

// Otras formas de agregar elementos al arreglo
autos[autos.length] = 'Porche';
console.log(autos);

// Tercera forma de agregar elementos teniendo CUIDADO
autos[6] = 'Renault';
console.log(autos);

// 1.4 Como preguntar si es un Array o un Arreglo
console.log(Array.isArray(autos)); //Devuelve un booleano

console.log(autos instanceof Array); //Preguntamos si la variable es una instancia de la clase Array
