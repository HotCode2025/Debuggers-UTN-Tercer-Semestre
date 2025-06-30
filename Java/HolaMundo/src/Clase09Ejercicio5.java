
import java.util.Scanner;

//Clase09_Ejercicio5
public class Clase09Ejercicio5 { public static void main(String[] args) {
    /*
Ejercicio 5: Hacer un programa que calcule e impirma la suma de tres calificacoines
Pedir las calificaciones al usuario
*/
        Scanner scanner = new Scanner(System.in);
        double suma = 0;

        for (int i = 0; i < 3; i++) {
            System.out.print("Ingrese la calificación número " + (i + 1) + ": ");
            double calificaciones = scanner.nextDouble();
            suma =  suma + calificaciones;
        }
        System.out.println("La suma de las calificaciones es: " + suma);
        scanner.close();
     }
    
}
