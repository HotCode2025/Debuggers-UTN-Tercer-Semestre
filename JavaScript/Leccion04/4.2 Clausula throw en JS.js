// 4.2 Cláusula throw en JS
// De esta manera es que podemos reportar nuestros propios errores con la cláusula throw.

let resultado = '';

try {
    y = 5;
    if (isNaN(resultado)) throw 'El resultado no es un numero'; // Si el resultado no es un numero, lanzamos un error
    else if (resultado === '') throw 'El resultado esta vacio'; // Si el resultado esta vacio, lanzamos un error
    else if (resultado >= 0) throw 'El resultado es positivo'; // Si el resultado es positivo, lanzamos un error
    else if (resultado < 0) throw 'El resultado es negativo'; // Si el resultado es negativo, lanzamos un error
}

catch (error) {
    console.log(error);
    console.log(error.name);
    console.log(error.message);
}finally {
    console.log('Fin de la revision de errores');
}