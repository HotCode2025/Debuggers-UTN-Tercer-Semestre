// 1.6 Comenzamos las pruebas creando objetos de cada clase y las agregamos a la lista de Orden: Parte 1, 2 y 3
package mundopc;

import ar.com.system2023.mundopc.*;


public class mundoPC {
    public static void main(String[] args) {
        Monitor monitorHP = new Monitor("HP", 13); // Importar la clase
        Teclado tecladoHP = new Teclado("Bluetooth", "HP");
        Raton ratonHP = new Raton("Bluetooth", "HP");
        Computadora computadoraHP = new Computadora("Computadora HP", monitorHP, tecladoHP, ratonHP);
        
        //Creamos otros objetos de diferente marca
        Monitor monitorGamer = new Monitor("Gamer", 32);
        Teclado tecladoGamer = new Teclado("Bluetooth", "Gamer");
        Raton ratonGamer = new Raton("Bluetooth", "Gamer");
        Computadora computadoraGamer = new Computadora("Computadora Gamer", monitorGamer, tecladoGamer, ratonGamer);
        
        Monitor monitorExo = new Monitor("Exo", 24);
        Teclado tecladoExo = new Teclado("Bluetooth", "Exo");
        Raton ratonExo = new Raton("Bluetooth", "Exo");
        Computadora computadoraExo = new Computadora("Computadora Exo", monitorExo, tecladoExo, ratonExo);
        
        Monitor monitorAsus = new Monitor("Asus", 34);
        Teclado tecladoAsus = new Teclado("Bluetooth", "Asus");
        Raton ratonAsus = new Raton("Bluetooth", "Asus");
        Computadora computadoraAsus = new Computadora("Computadora Asus", monitorAsus, tecladoAsus, ratonAsus);
        
        
        Computadora computadorasVarias = new Computadora("Computadora de diferentes marcas", monitorHP, tecladoGamer, ratonHP);
        Computadora computadorasEconom = new Computadora("Computadora de economicas", monitorExo, tecladoAsus, ratonHP);
        
        // Lista de ordenes (Arreglos vacios)
        Orden orden1 = new Orden(); // Inicializamos el arreglo vacio
        Orden orden2 = new Orden(); // Una nueva lista para el objeto orden2
        Orden orden3 = new Orden(); // Orden3 
        
        // Completamos las ordenes creadas
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraGamer);
        orden1.agregarComputadora(computadorasVarias);
        orden1.agregarComputadora(computadoraExo);
        orden1.agregarComputadora(computadoraAsus);
        orden1.agregarComputadora(computadorasEconom);
        orden1.agregarComputadora(computadoraGamer);
        orden1.agregarComputadora(computadorasVarias);
        orden1.agregarComputadora(computadoraExo);
        orden1.agregarComputadora(computadoraAsus);
       
        orden2.agregarComputadora(computadorasVarias);
        orden2.agregarComputadora(computadorasEconom);
        
        orden3.agregarComputadora(computadoraHP);
        orden3.agregarComputadora(computadoraExo);
        orden3.agregarComputadora(computadoraAsus);
        
        // Se muestran las ordenes creadas 
        orden1.mostrarOrden();
        orden2.mostrarOrden();
        orden3.mostrarOrden();
        
        // Crear mas objetos de tipo computadora con todos sus elementos
        // Completar una lista en el objeto orden1 que llegue a los 10 elementos
        // Probar de esta manera los metodos al maximo rendimiento
    }
}
