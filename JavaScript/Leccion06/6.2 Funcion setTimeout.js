// 6.2 Función setTimeout

// Llamadas asíncronas con setTimeout 
function miFuncionCallback(){
    console.log("Saludo asincronico después de 3 segundos");
}

setTimeout(miFuncionCallback, 3000); // Saludo asincronico después de 3 segundos

setTimeout(function(){ console.log("Saludo asincronico 2")}, 5000); // Saludo asincronico 2

setTimeout(() => console.log("Saludo asincronico 3"), 7000); // Saludo asincronico 3

console.log("--------------------------------------------------");