class NReinasVisual {
    constructor(n, velocidad) {
        this.n = n;
        this.velocidad = velocidad; // Tiempo en milisegundos para pausar la animación
        this.reinas = new Array(this.n).fill(-1); 
        this.solucionEncontrada = false;
        
        this.contenedor = document.getElementById("contenedor-tablero");
        this.txtEstado = document.getElementById("estado");
        this.txtIndices = document.getElementById("arreglo-indices");
        
        this.inicializarTableroHTML();
    }

    // Crea la cuadrícula vacía en el HTML
    inicializarTableroHTML() {
        this.contenedor.innerHTML = ""; 
        this.txtIndices.innerHTML = "";
        
        const tableroHTML = document.createElement("div");
        tableroHTML.className = "tablero";
        // Definimos el tamaño del tablero según N
        tableroHTML.style.gridTemplateColumns = `repeat(${this.n}, 50px)`;
        tableroHTML.style.gridTemplateRows = `repeat(${this.n}, 50px)`;

        for (let fila = 0; fila < this.n; fila++) {
            for (let col = 0; col < this.n; col++) {
                const celda = document.createElement("div");
                celda.id = `celda-${fila}-${col}`;
                
                // Alternamos colores para simular un tablero de ajedrez
                if ((fila + col) % 2 === 0) {
                    celda.className = "celda blanca";
                } else {
                    celda.className = "celda negra";
                }
                
                tableroHTML.appendChild(celda);
            }
        }
        this.contenedor.appendChild(tableroHTML);
    }

    // Función auxiliar para generar pausas
    esperar() {
        return new Promise(resolve => setTimeout(resolve, this.velocidad));
    }

    // Método principal
    async resolver() {
        this.txtEstado.innerText = `=== Buscando solución para N = ${this.n} ===`;
        this.txtEstado.style.color = "#2c3e50";
        
        let exito = await this.buscarSolucion(0);
        
        if (exito) {
            this.txtEstado.innerText = "🎉 ¡SOLUCIÓN ENCONTRADA CON ÉXITO! 🎉";
            this.txtEstado.style.color = "#2ecc71";
            this.mostrarIndicesFinales();
        } else {
            this.txtEstado.innerText = "❌ No se encontró ninguna solución.";
            this.txtEstado.style.color = "#e74c3c";
        }
    }

    // -------------------------------------------------------------------------------------
    async buscarSolucion(fila) {
        if (fila === this.n) {
            this.solucionEncontrada = true;
            return true;
        }

        for (let col = 0; col < this.n; col++) {
            this.marcarFilaEnPrueba(fila, col);
            await this.esperar(); // Pausa para ver la linea

            if (this.esSeguro(fila, col)) {
                this.reinas[fila] = col; 
                
                this.dibujarReinaEnCelda(fila, col, "👑"); 
                this.desmarcarFilaEnPrueba(fila);

                if (await this.buscarSolucion(fila + 1)) {
                    return true; 
                }

                // Si falló la solución removemos la reina
                this.dibujarReinaEnCelda(fila, col, ""); 
                this.reinas[fila] = -1; 
            }
            
            this.desmarcarFilaEnPrueba(fila);
        }
        return false;
    }

    esSeguro(fila, col) {
        for (let i = 0; i < fila; i++) {
            let colReinaExistente = this.reinas[i];
            if (colReinaExistente === col) return false;
            if (Math.abs(i - fila) === Math.abs(colReinaExistente - col)) return false;
        }
        return true;
    }

    dibujarReinaEnCelda(fila, col, emoji) {
        const celda = document.getElementById(`celda-${fila}-${col}`);
        if (celda) {
            celda.innerText = emoji;
            if (emoji) celda.classList.add("reina");
            else celda.classList.remove("reina");
        }
    }

    marcarFilaEnPrueba(filaActual, colActual) {
        // Marcamos la celda que se está testeando
        const celda = document.getElementById(`celda-${filaActual}-${colActual}`);
        if (celda) celda.classList.add("probando");
    }

    desmarcarFilaEnPrueba(filaActual) {
        for (let col = 0; col < this.n; col++) {
            const celda = document.getElementById(`celda-${filaActual}-${col}`);
            if (celda) celda.classList.remove("probando");
        }
    }

    // Muestra la solución encontrada
    mostrarIndicesFinales() {
        const filaFormat = this.reinas.map((_, i) => `[${i}]`).join("  ");
        const colFormat = this.reinas.map(v => `&nbsp;${v}&nbsp;`).join("  ");
        
        this.txtIndices.innerHTML = `
            <p><strong>Arreglo de Índices Planteados:</strong></p>
            <div style="font-family: monospace; background: #eec; padding: 10px; display:inline-block; border-radius:5px;">
                Filas (Índices):&nbsp;&nbsp;&nbsp;&nbsp; ${filaFormat}<br>
                Columnas (Valores): ${colFormat}
            </div>
        `;
    }
}
