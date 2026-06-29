setTimeout(miFuncionCallback, 3000);

setTimeout(function() { console.log('Saludo asincrono 2'); }, 4000);

setTimeout(() => console.log('Saludos Asincrono 3'), 5000);

let reloj = () => {
    let fecha = new Date();
    
    console.log(`${fecha.getHours()}:${fecha.getMinutes()}:${fecha.getSeconds()}`);
}

setInterval(reloj,1000); //Cada 1 segundo se ejecuta 
