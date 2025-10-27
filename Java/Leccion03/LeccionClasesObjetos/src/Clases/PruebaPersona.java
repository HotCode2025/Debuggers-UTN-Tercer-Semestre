package Clases;

public class PruebaPersona {

    public static void main(String[] args) {
        // 4.2 Creación de un Objeto
        Persona persona1;
        persona1 = new Persona(); //Llamamos al constructor
        persona1.nombre = "Jairo"; // El valor hexadecimal normalmente comienza con 0x 
        persona1.apellido = "Ubilla";
        persona1.obtenerInformacion();
        
        // 4.3 Creación de un Objeto más
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformacion();
        persona2.nombre = "Wilson";
        persona2.apellido = "Godoy";
        persona2.obtenerInformacion();
    }
}
