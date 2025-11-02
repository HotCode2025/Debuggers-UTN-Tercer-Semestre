//10.4 Uso de la palabra reservada final, Parte 1 a la Parte 4
package domain;


public class Persona {
    public final static int CONSTANTE_AQUI = 15;
    private String nombre;

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    
    public void imprimir() {
        System.out.println("Metodo para imprimir");
    }
}
