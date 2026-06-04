const cantidadDiscos = 4;

const colores = [
    "#E67E22", // naranja
    "#F1C40F", // amarillo
    "#2ECC71", // verde
    "#3498DB", // azul
    "#9B59B6", // violeta
    "#E74C3C", // rojo
    "#1ABC9C", // turquesa
    "#D35400"  // marrón
];

const torres = {
    A: [],
    B: [],
    C: []
};

const movimientos = [];

function resolverHanoi(n, origen, auxiliar, destino){

    if(n === 1){
        movimientos.push([origen, destino]);
        return;
    }

    resolverHanoi(n-1, origen, destino, auxiliar);

    movimientos.push([origen, destino]);

    resolverHanoi(n-1, auxiliar, origen, destino);
}

function crearDiscos(){

    for(let i = cantidadDiscos; i >= 1; i--){
        torres.A.push(i);
    }

    dibujarTorres();
}

function dibujarTorres(){

    ["A","B","C"].forEach(nombre => {

        const contenedor = document.getElementById(nombre);

        contenedor.innerHTML = "";

        torres[nombre].forEach(disco => {

            const div = document.createElement("div");

            div.classList.add("disco");

            div.style.width = `${40 + disco * 25}px`;

            div.style.backgroundColor = colores[disco - 1];

            contenedor.appendChild(div);
        });
    });
}

function moverDisco(origen, destino){

    const disco = torres[origen].pop();

    torres[destino].push(disco);

    dibujarTorres();
}

async function ejecutarMovimientos(){

    const texto = document.getElementById("movimientos");

    for(let i=0; i<movimientos.length; i++){

        let [origen, destino] = movimientos[i];

        moverDisco(origen, destino);

        texto.innerHTML =
        `Movimiento ${i+1}: ${origen} ➜ ${destino}`;

        await new Promise(resolve =>
            setTimeout(resolve, 800)
        );
    }

    texto.innerHTML +=
    "<br><br>✅ Torre completada";
}

document.getElementById("iniciar")
.addEventListener("click", () => {

    movimientos.length = 0;

    torres.A = [];
    torres.B = [];
    torres.C = [];

    crearDiscos();

    resolverHanoi(
        cantidadDiscos,
        "A",
        "B",
        "C"
    );

    ejecutarMovimientos();
});

crearDiscos();