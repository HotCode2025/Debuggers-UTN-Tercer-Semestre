class NReinasConsola {
    constructor(n, elementoTerminal, velocidad) {
        if (n < 8) { 
            this.n = 8; 
            this.elementoTerminal = elementoTerminal;
            this.print("⚠️ El valor mínimo para calcular soluciones es 8. Ajustando a 8...\n");
        } else {
            this.n = n;
            this.elementoTerminal = elementoTerminal;
        }
        this.velocidad = velocidad; // Tiempo en milisegundos de la pausa
        this.reinas = new Array(this.n).fill(-1); 
        this.solucionEncontrada = false;
    }

    print(texto) {
        if (this.elementoTerminal) {
            this.elementoTerminal.innerHTML += texto + "\n";
            this.elementoTerminal.scrollTop = this.elementoTerminal.scrollHeight;
        }
        console.log(texto);
    }

    // Pausamos un momento el hilo de ejecución para poder ver los cambios
    esperar() {
        return new Promise(resolve => setTimeout(resolve, this.velocidad));
    }

    // Usamos un método asíncrono para permitir pausas
    async resolver() {
        this.print(`=== INICIANDO BÚSQUEDA PARA N = ${this.n} ===`);
        this.print(`Velocidad de simulación: ${this.velocidad}ms por intento.\n`);
        await this.esperar();
        await this.buscarSolucion(0);
    }

    async buscarSolucion(fila) {
        if (fila === this.n) {
            this.solucionEncontrada = true;
            this.mostrarTableroFinal();
            return true;
        }

        for (let col = 0; col < this.n; col++) {
            if (this.esSeguro(fila, col)) {
                this.reinas[fila] = col; 

                // Mostramos las pruebas en el navegador
                this.mostrarTableroEnConstruccion(fila);
                
                await this.esperar();
                if (await this.buscarSolucion(fila + 1)) {
                    return true; 
                }

                // Si no funcionó, imprimimos el retroceso antes de limpiar
                this.print(`↩️ Celda inválida en fila ${fila + 1}, columna ${col + 1}. Retrocediendo...\n`);
                this.reinas[fila] = -1; 
                await this.esperar();
            }
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

    mostrarTableroEnConstruccion(filaActual) {
        this.print(`Probando posición en Fila ${filaActual + 1}:`);
        let vista = "";
        for (let i = 0; i < this.n; i++) {
            let linea = "  ";
            for (let j = 0; j < this.n; j++) {
                if (this.reinas[i] === j) {
                    linea += "👑 ";
                } else if (i === filaActual) {
                    linea += "❌ ";
                } else {
                    linea += "·  ";
                }
            }
            vista += linea + "\n";
        }
        this.print(vista);
    }

    mostrarTableroFinal() {
        this.print("\n=============================================");
        this.print("        ¡SOLUCIÓN ENCONTRADA CON ÉXITO!        ");
        this.print("=============================================\n");

        this.print("TABLERO TERMINADO:");
        let tableroVisual = "";
        for (let i = 0; i < this.n; i++) {
            let linea = `Fila ${i}: `;
            for (let j = 0; j < this.n; j++) {
                linea += (this.reinas[i] === j) ? "👑 " : "·  ";
            }
            tableroVisual += linea + "\n";
        }
        this.print(tableroVisual);

        this.print("ARREGLO DE ÍNDICES PLANTEADOS:");
        this.print("Índices (Filas):    " + this.reinas.map((_, i) => `[${i}]`).join(" "));
        this.print("Valores (Columnas): " + this.reinas.map(v => ` ${v} `).join(" "));
        this.print("\n=============================================");
    }
}