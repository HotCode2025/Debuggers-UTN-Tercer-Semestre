//12.1 Manejo de Matrices Parte 1: Aquí creamos la carpeta Leccion10
package test;

import domain.Persona;

public class TestMatrices {

    public static void main(String[] args) {
        int edades[][] = new int[4][4];
        System.out.println("edades = " + edades);
        edades[0][0] = 5; //Llenado manual
        edades[0][1] = 4;
        edades[0][2] = 3;
        edades[0][3] = 6; //Es una diferente columna

        //12.2 Manejo de Matrices Parte 2: Hacer la tarea
        edades[1][0] = 7;//Terminamos la tarea
        edades[1][1] = 8;
        edades[1][2] = 9;
        edades[1][3] = 1;
        edades[2][0] = 2;
        edades[2][1] = 3;
        edades[2][2] = 6;
        edades[2][3] = 8;

        System.out.println("edades 0-0 = " + edades[0][0]);
        System.out.println("edades 0-1 = " + edades[0][1]);
        System.out.println("edades 0-2 = " + edades[0][2]);
        System.out.println("edades 0-3 = " + edades[0][3]);
        System.out.println("edades 1-0 = " + edades[1][0]);
        System.out.println("edades 1-1 = " + edades[1][1]);
        System.out.println("edades 1-2 = " + edades[1][2]);
        System.out.println("edades 1-3 = " + edades[1][3]);
        System.out.println("edades 2-0 = " + edades[2][0]);
        System.out.println("edades 2-1 = " + edades[2][1]);
        System.out.println("edades 2-2 = " + edades[2][2]);
        System.out.println("edades 2-3 = " + edades[2][3]);

        //12.3 Manejo de Matrices Parte 3: Ciclo for iterando
        System.out.println("Recorremos la matriz a traves del ciclo for");

        for (int fila = 0; fila < edades.length; fila++) {
            for (int col = 0; col < edades[fila].length; col++) {
                System.out.println("Edades " + fila + "-" + col + ": " + edades[fila][col]);

            }
        }

        // 12.4 Manejo de Matrices Parte 4: Sintaxis simplificada
        //Sintaxis clasica
        //String frutas[][] = new String[3][2];
        //Sintaxis Simplificada
        String frutas[][] = {{"Limon", "Pomelo"}, {"Ciruela", "Kiwi"}, {"Banana", "Manzana"}};
        imprimir(frutas);

//        for (int i = 0; i < frutas.length; i++) {
//            for (int col = 0; col < frutas[i].length; col++) {
//                System.out.println("frutas " + i + "-" + col + ": " + frutas[i][col]);
//            }
//        }
        // 12.5 Manejo de Matrices Parte 5: Matriz de objetos, creamos un método
        // Creamos una matriz de objetos
        Persona personas[][] = new Persona[2][3];
        //Asignamos valores a la matriz
        personas[0][0] = new Persona("Jairo");
        personas[0][1] = new Persona("Osvaldo");
        personas[0][2] = new Persona("Wilson");
        personas[1][0] = new Persona("Pepe");
        personas[1][1] = new Persona("Tito");
        personas[1][2] = new Persona("Oscar");
        System.out.println("Matriz de Personas: ");
        imprimir(personas);
    }

    public static void imprimir(Object matriz[][]) {
        for (int i = 0; i < matriz.length; i++) {
            for (int col = 0; col < matriz[i].length; col++) {
                System.out.println("frutas " + i + "-" + col + ": " + matriz[i][col]);
            }
        }
    }
}
