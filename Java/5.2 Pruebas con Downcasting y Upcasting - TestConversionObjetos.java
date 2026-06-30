package test;

import domain.*;

public class TestConversionObjetos {
    public static void main(String[] args) {
        Empleado empleado;
        empleado = new Escritor("Juan", 5000, TipoEscritura.CLASICO);
        System.out.println("empleado = " + empleado);
        System.out.println(empleado.obtenerDetalles()); 
        
        // Downcasting
        ((Escritor)empleado).getTipoEscritura(); // Opcion 1
        
        Escritor escritor = (Escritor)empleado; // Opcion 2
        escritor.getTipoEscritura();

        // Upcasting
        Empleado empleado2 =  escritor;
        System.out.println(empleado2.obtenerDetalles());
        
    }
}
