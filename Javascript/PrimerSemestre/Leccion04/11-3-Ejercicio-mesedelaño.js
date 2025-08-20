//Hacer un ejercicio similar al que esta hecho, pero ahora con los 
//meses del año, debes hacerlo con la estructura switch  luego con
//la funcion en la opcion mejorada

let mes = 6;
switch (mes) {
    case 1:
        console.log("El mes es Enero");
        break;
    case 2:
        console.log("El mes es Febrero");
        break
    case 3:
        console.log("El mes es Marzo");
        break
    case 4:
        console.log("El mes es Abril");
        break
    case 5:
        console.log("El mes es Mayo");
        break
    case 6:
        console.log("El mes es Junio");
        break
    case 7:
        console.log("El mes es Julio");
        break;
    case 8:
        console.log("El mes es Agosto");
        break
    case 9:
        console.log("El mes es Septiembre");
        break
    case 10:
        console.log("El mes es Octubre");
        break;
    case 11:
        console.log("El mes es Noviembre");
        break
    case 12:
        console.log("El mes es Diciembre");
        break
     default:
        console.log("Error en el ingreso del mes");
        break;
}


//Esta es la opcion mejorada

let mes2 = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"];
function getDay(n){
    if(n < 1 || n > 12){
        throw new Error("out of range");
    }
    return mes2[n-1];
}
console.log(getDay(6));