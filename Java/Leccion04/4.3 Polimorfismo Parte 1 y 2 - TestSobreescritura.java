package test;

import domain.*;

public class TestSobreescritura {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Juan", 10000);
//        System.out.println("empleado1 = " + empleado1.obtenerDetalles());
        imprimir(empleado1);
        
        Gerente gerente1 = new Gerente("Jose", 5000, "Sistemas");
//        System.out.println("gerente1 = " + gerente1.obtenerDetalles());
        imprimir(gerente1);
    }
    
    public static void imprimir(Empleado empleado) {
            System.out.println("empleado = " + empleado.obtenerDetalles());
    }
}
