// Clase base para dispositivos de entrada (teclado, ratón)
class DispositivoEntrada {
    constructor(tipoEntrada, marca) {
        this._tipoEntrada = tipoEntrada; // Ej: USB, Bluetooth
        this._marca = marca;
    }

    get tipoEntrada() {
        return this._tipoEntrada;
    }

    set tipoEntrada(tipoEntrada) {
        this._tipoEntrada = tipoEntrada;
    }

    get marca() {
        return this._marca;
    }

    set marca(marca) {
        this._marca = marca;
    }
}

// -------------------------------------------------- //

// Representa un monitor
class Monitor {
    static contadorMonitores = 0;

    constructor(marca, tamanio) {
        this._idMonitor = ++Monitor.contadorMonitores; // ID autoincremental
        this._marca = marca;
        this._tamanio = tamanio;
    }

    get idMonitor() {
        return this._idMonitor;
    }

    toString() {
        return `Monitor: [idMonitor: ${this._idMonitor}, marca: ${this._marca}, tamaño: ${this._tamanio}]`;
    }
}

// -------------------------------------------------- //

// Representa un teclado (hereda de DispositivoEntrada)
class Teclado extends DispositivoEntrada {
    static contadorTeclado = 0;

    constructor(tipoEntrada, marca) {
        super(tipoEntrada, marca);
        this._idTeclado = ++Teclado.contadorTeclado;
    }

    get idTeclado() {
        return this._idTeclado;
    }

    toString() {
        return `Teclado: [idTeclado: ${this._idTeclado}, tipoEntrada: ${this._tipoEntrada}, marca: ${this._marca}]`;
    }
}

// -------------------------------------------------- //

// Representa un ratón (hereda de DispositivoEntrada)
class Raton extends DispositivoEntrada {
    static contadorRatones = 0;

    constructor(tipoEntrada, marca) {
        super(tipoEntrada, marca);
        this._idRaton = ++Raton.contadorRatones;
    }

    get idRaton() {
        return this._idRaton;
    }

    toString() {
        return `Raton: [idRaton: ${this._idRaton}, tipoEntrada: ${this._tipoEntrada}, marca: ${this._marca}]`;
    }
}

// -------------------------------------------------- //

// Representa una computadora compuesta por monitor, teclado y ratón
class Computadora {
    static contadorComputadoras = 0;

    constructor(nombre, monitor, teclado, raton) {
        this._idComputadora = ++Computadora.contadorComputadoras;
        this._nombre = nombre;
        this._monitor = monitor;
        this._teclado = teclado;
        this._raton = raton;
    }

    toString() {
        return `Computadora ${this._idComputadora}: ${this._nombre}
            ${this._monitor}
            ${this._teclado}
            ${this._raton}`;
    }
}

// -------------------------------------------------- //

// Representa una orden que contiene varias computadoras
class Orden {
    static contadorOrdenes = 0;

    constructor() {
        this._idOrden = ++Orden.contadorOrdenes;
        this._computadoras = []; // Lista de computadoras
    }

    get idOrden() {
        return this._idOrden;
    }

    // Agrega una computadora a la orden
    agregarComputadora(computadora) {
        this._computadoras.push(computadora);
    }

    // Muestra todas las computadoras de la orden
    mostrarOrden() {
        let computadorasOrden = '';

        for (let computadora of this._computadoras) {
            computadorasOrden += `\n${computadora}`;
        }

        console.log(`Orden: ${this._idOrden}, Computadoras: ${computadorasOrden}`);
    }
}