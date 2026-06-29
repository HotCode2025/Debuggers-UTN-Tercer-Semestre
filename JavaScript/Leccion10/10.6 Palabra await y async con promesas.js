// async indica que una funcion regresa una promesa

async function miFuncionConPromesa(){
    return "Saludos con promesa y async";
}

//miFuncionConPromesa().then(valor => console.log(valor));

//async/await
async function funcionConPromesaYAwait(){
  let miPromesa = new Promise(resolver => {
  });
  console.log(await miPromesa); 
}

funcionConPromesaYAwait();

