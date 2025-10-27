/* 4.7 Ejercicio con Ciclos 7 Con la Clase Scanner y JOptionPane
Ejercicio 7: pedir números hasta que se introduzca uno negativo
Calcular la media
 */
package Ciclos07;

import java.util.Scanner;

public class Ciclos07 {

    public static void main(String[] args) {
        int numero, suma = 0, contador = 0;

        Scanner entrada = new Scanner(System.in);

        System.out.print("Ingresar un número (número negativo para fin): ");
        numero = entrada.nextInt();

        while (numero >= 0) {
            suma += numero;
            contador++;
            System.out.print("Ingresar un número (número negativo para fin): ");
            numero = entrada.nextInt();
        }

        if (contador > 0) {
            double media = (double) suma / contador;
            System.out.println("La media de los números ingresados es: " + media);
        }
    }
}
