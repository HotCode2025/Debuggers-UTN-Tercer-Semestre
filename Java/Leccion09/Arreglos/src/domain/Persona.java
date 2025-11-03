//11.4 Arreglos Parte 4
package domain;

public class Persona {

    private String nombre;

    public Persona(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return this.nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    //11.5 Agregamos el toString

    @Override
    public String toString() {
        return "Persona{" + "nombre=" + nombre + '}' + ", " + super.toString();
    }

}
