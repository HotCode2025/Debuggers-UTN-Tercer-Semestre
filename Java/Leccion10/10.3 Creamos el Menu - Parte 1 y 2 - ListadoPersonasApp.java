
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ListadoPersonasApp {
    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        // Definismo la lista fuera del ciclo while
        List<Persona> personas = new ArrayList<>();
        
        // Menu
        var salir = false;
        while(!salir) {
            mostrarMenu();
            System.out.println("");
        } // Fin ciclo while
    } // Fin metod main
    
    private static void mostrarMenu() {
        // Mostramos las opciones
        System.out.print("""
                        *****    Listado de Persona *****
                         1. Agregar
                         2. Listar
                         3. Salir
                           """);
        System.out.print("Digite una de las opciones: ");
    }
    
}
