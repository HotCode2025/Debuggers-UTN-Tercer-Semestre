//13.7 Comenzamos con las pruebas en VentasTest
package ar.com.codesystem.test;

import ar.com.codesystem.ventas.Orden;
import ar.com.codesystem.ventas.Producto;

public class VentasTest {

    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 19870.88);
        Producto producto2 = new Producto("Campera", 34890);

        Orden orden1 = new Orden();
        Orden orden2 = new Orden();
        Orden orden3 = new Orden();

        //Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();

        //Tarea:
        //Crear mas objetos de tipo Producto = 10
        //Crear mas objetos de tipo orden = 2
        Producto producto3 = new Producto("Playera", 17870.88);
        Producto producto4 = new Producto("Camperon", 36890);
        Producto producto5 = new Producto("Remera", 19870.88);
        Producto producto6 = new Producto("Medias", 34890);
        Producto producto7 = new Producto("Zapatos", 19870.88);
        Producto producto8 = new Producto("Zapatillas", 34890);
        Producto producto9 = new Producto("Gorra", 11870.88);

        orden1.agregarProducto(producto4);
        orden1.agregarProducto(producto3);
        orden1.mostrarOrden();

        orden2.agregarProducto(producto9);
        orden2.agregarProducto(producto8);
        orden2.mostrarOrden();

        orden3.agregarProducto(producto5);
        orden3.agregarProducto(producto6);
        orden3.mostrarOrden();

    }
}
