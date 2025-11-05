//11.6 Arreglos Parte 5 y 6: Veamos como iterar en Java
package test;

import domain.Persona;

public class TestArregloObject {

    public static void main(String[] args) {
        Persona personas[] = new Persona[2];
        personas[0] = new Persona("Jairo");
        personas[1] = new Persona("Wilson");
        System.out.println("personas 0 = " + personas[0]);
        System.out.println("personas 1 = " + personas[0]);

        for (int i = 0; i < personas.length; i++) {
            System.out.println("personas  " + i + " 0 " + personas[1]);
        }

        //Trabajamos con arreglos en la sintaxisreumida
        String frutas[] = {"Banana", "Pera", "Durazno"};
        for (int i = 0; i < frutas.length; i++) {
            System.out.println("frutas " + i + " = " + frutas[i]);
        }
    }
}
