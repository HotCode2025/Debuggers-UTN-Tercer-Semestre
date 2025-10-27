/** 4.5 Ejercicio con Ciclos 6 Clase Scanner y JOptionPane
 * Ejercicio 6: Pedir numeros hasta que se teclee n 0
 * mostrar la suma de todos los numeros introducidos
 */
package Ciclos06;

import java.util.Scanner;

public class Ciclos06 {

    public static void main(String[] args) {
        int numero;
        int suma = 0;

        Scanner entrada = new Scanner(System.in);

        System.out.println("Ingresar un número (0 para fin): ");
        numero = entrada.nextInt();

        do {
            suma = suma + numero;
            System.out.println("Ingresa un número (0 para fin): ");
            numero = entrada.nextInt();
        } while (numero != 0);

        System.out.println("La suma de todos los números es: " + suma);
    }
}
