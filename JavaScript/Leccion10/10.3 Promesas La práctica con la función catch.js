let miPromesa = new Promise( (resolver, rechazar) => {
    let expresion = true;
    if (expresion) {
        resolver('Resolvio correctamente');
    } else {
            rechazar('Se produjo un error');
        }
    }
);

miPromesa
    .then( valor => console.log(valor))
    .catch(error => console.log(error));