//11.1 Arreglos Parte 1: Creamos la carpeta Leccion9
package test;

public class TestArreglos {

    public static void main(String[] args) { //Lado der. instanciamos un objeto de tipo object
        int edades[] = new int[3]; // El lado izq. declaramos la variable
        System.out.println("edades = " + edades);

        // 11.2 Arreglos Parte 2
        edades[0] = 17;
        System.out.println("edades 0 = " + edades[0]);

        edades[1] = 18;
        System.out.println("edades 1 = " + edades[1]);

        edades[2] = 16;
        System.out.println("edades 2 = " + edades[2]);
        
        //11.3 Arreglos Parte 3
        //edades[3] = 7; // Fuera de rango, error en tiempo de ejecución
        for (int i = 0; i < edades.length; i++) {
            System.out.println("Edades y sus elementos " + i + ": " + edades[i]);
        }
    }
}
