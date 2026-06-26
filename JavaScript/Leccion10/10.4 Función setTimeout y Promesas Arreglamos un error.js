//10.4 Función setTimeout y Promesas -> Arreglamos un error

let promesa = new Promise( (resolver) =>{
    console.log('Inicio promesa');
    setTimeout(()=> resolver('Saludos desde promesa, callback, funcion flecha y setTimeout'), 3000);
    console.log('Final promesa');
});

//El llamado a la promesa
promesa.then( valor => console.log(valor));