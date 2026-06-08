// 1.4 Manejo de bloques de código
// Video 01
package domain;


public class Persona {
    private final int idPersona;
    private static int contadorPersonas;
    
    static{ //Bloque de inicialización estático
        System.out.println("Ejecución del bloque estático");
        ++Persona.contadorPersonas;
        //idPersona=10; No es un atributo estático, nos va a dar error
    }