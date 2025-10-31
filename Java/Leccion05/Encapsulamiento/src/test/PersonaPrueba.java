//8.1 Encapsulamiento Parte 2: hacer tarea
package test;

import dominio.Persona;

public class PersonaPrueba {

    public static void main(String[] args) {
        Persona persona1 = new Persona("Pepe", 75.000, false);
        System.out.println("persona1 = " + persona1); //8.3 Método toString
        System.out.println("persona1 su nombre es: " + persona1.getNombre());
        //Modificar a través de los métodos
        persona1.setNombre("Juan cruz");
        //persona1.nombre = "Juan"; //Ya no se puede utilizar
        //System.out.println("Nombre es: "+ persona1.nombre); //Error
        System.out.println("persona1 con su nombre modificado: " + persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: " + persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: " + persona1.isEliminado());
        //Tarea: Crear otro objeto de tipo Persona, asignar valores de manera inicial
        //e imprimir, luego modificar sus valores y volver a imprimir

        Persona persona2 = new Persona("Jorge", 712.000, false);
        System.out.println("persona2 su nombre es: " + persona2.getNombre());
        System.out.println("persona2 el resultado para el sueldo: " + persona2.getSueldo());
        System.out.println("persona2 para obtener el booleano: " + persona2.isEliminado());

        persona2.setNombre("Alejandro");
        persona2.setSueldo(650.000);
        persona2.setEliminado(true);
        System.out.println("persona2 con su nombre modificado: " + persona2.getNombre());
        System.out.println("persona2 el resultado para el sueldo modificado: " + persona2.getSueldo());
        System.out.println("persona2 para obtener el booleano modificado: " + persona2.isEliminado());

        //8.2 Encapsulamiento Parte 3
        //8.3 Método toString
        System.out.println("persona2 = " + persona2);
        //8.4 Contexto estático teoría
    }
}
