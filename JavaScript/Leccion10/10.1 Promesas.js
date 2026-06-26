let miPromesa = new Promise( (resolver, rechazar) => {
    let expresion = true;
    if (expresion){
        resolver('Resolvio Correctamente');
    } else{
        rechazar('Se Produjo un error');
    }
});

miPromesa.then(
    valor => console.log(valor),
    error => console.log(error)
);



