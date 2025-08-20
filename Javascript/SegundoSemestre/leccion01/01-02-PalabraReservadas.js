// Palabra reservada break
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 == 0){
        console.log(contando);
        break;
    }
}
console.log("Termina el ciclo al encontrar el primer numero par");

// La palabra continue
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        continue; // ir a la siguiente iteracion
    }
    console.log(contando);
}
console.log("Termina el ciclo");