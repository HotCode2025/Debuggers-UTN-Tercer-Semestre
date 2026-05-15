package domain;

/*
 * @author UTN Debuggers
 */

public class Persona {
    private final int idPersona;
//    private static int contadoPersonas;
/*    
    // Bloque de inicializacion estatico
    static {
        System.out.println("Ejecución del bloque estático");
        ++Persona.contadoPersonas;
        // idPersona = 10; Esto da error porque no es un atributo estatico
    }
*/

    // Reemplazamos el Bloque Estatico 
    // Usamos un método estático privado para inicializar la variable.
    private static int contadoPersonas = inicializarContadorEstatico();
    
    private static int inicializarContadorEstatico() {
        System.out.println("Ejecución de inicialización estática (Método)");
        // En el código original hacíamos ++Persona.contadoPersonas
        // partiendo de 0, lo que daba 1. Así que retornamos 1.
        return 1; 
    }
    
   /*
    // Bloque de inicialización no estático (onctexto dinámico)
    {
        System.out.println("Ejecución del bloque NO estático");
        this.idPersona = Persona.contadoPersonas++; // Incrementamos el atributo
    }
   */
    
    // Reemplazamos el Bloque NO Estatico 
    // Para esto movemos toda la lógica al inicio del Constructor.
    public Persona() {
        // Inicio de lo que era el bloque NO estático
        System.out.println("Ejecución del bloque NO estático (ahora en Constructor)");
        this.idPersona = Persona.contadoPersonas++; // Incrementamos el atributo
        
        System.out.println("Ejecución del constructor");
    }
    
    // Los bloques de inicialización se ejecutan antes del constructor

    public int getidPersona() {
        return this.idPersona;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + '}';
    }
    
 }
