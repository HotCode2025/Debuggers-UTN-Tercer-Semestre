// 8.5 Comenzamos a hacer pruebas con RuntimeException (unchecked)
package excepciones;


public class OperacionExcepcion extends RuntimeException{
    // Constructor
    public OperacionExcepcion(String mensaje){
        super (mensaje);
    }
}
