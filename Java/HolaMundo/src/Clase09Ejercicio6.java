/*
Clase 9 - Ejercicio 6: Guillermo tiene N dolares, Luis tiene la mitad de lo que posee Guillermo.
Juan tiene la mitad de lo que poseen Luis y Guillermo juntos. 
Hacer un programa que calcule e imprima la cantidad de dinero que tienen entre los 3

dolaresGuillermo = N
dolaresLuis = dolaresGuillermo / 2
dolaresJuan = (dolaresGuillermo + dolaresLuis) / s
dolaresTotal = dolaresGuillermo + dolaresLuis + dolaresJuan
*/
import java.util.Scanner;

public class Clase09Ejercicio6 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Solicitar la cantidad de dólares de Guillermo
        System.out.print("Ingrese la cantidad de dólares que tiene Guillermo: ");
        double dolaresGuillermo = scanner.nextDouble();

        // Calculo la cantidades de dólares de Luis y Juan
        double dolaresLuis = dolaresGuillermo / 2;
        double dolaresJuan = (dolaresGuillermo + dolaresLuis) / 2;
        
        // Calculo la cantidad total de dólares
        double dolaresTotal = dolaresGuillermo + dolaresLuis + dolaresJuan;

        // Muestro los resultados
        System.out.println("Guillermo tiene: " + dolaresGuillermo + " dólares");
        System.out.println("Luis tiene: " + dolaresLuis + " dólares");
        System.out.println("Juan tiene: " + dolaresJuan + " dólares");
        System.out.println("El total entre los tres es: " + dolaresTotal + " dólares");

        scanner.close();
    }
}
    

