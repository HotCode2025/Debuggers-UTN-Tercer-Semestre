//8.6 Contexto estático práctica Parte 2 Ejecutar con debug File
package test;

import domain.Persona;

public class PersonaPrueba {

    public static void main(String[] args) {
        Persona persona1 = new Persona("Jairo");
        System.out.println("persona1 = " + persona1);
        Persona persona2 = new Persona("Wilson");
        System.out.println("persona2 = " + persona2);
        imprimir(persona1);
        imprimir(persona2);
        //this.contador = 10; //No se puede referenciar desde un contexto estatico
        PersonaPrueba personaP1 = new PersonaPrueba();
        System.out.println(personaP1.getContador());
    }

    //8.7 Ejercicio con contexto estático
    public static void imprimir(Persona persona) {
        System.out.println("persona = " + persona);
    }
    private int contador;

    public int getContador() {
        imprimir(new Persona("Alison"));
        return this.contador;
    }
}
