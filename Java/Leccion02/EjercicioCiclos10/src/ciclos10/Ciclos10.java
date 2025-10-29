/*
Ejercicio 10: Pedir 10 números y escribir la suma 
total
Hacerlo con la clase Scanner y JOptionPane
 */
package ciclos10;

import java.util.Scanner;

public class Ciclos10 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int suma = 0;
        int numero;

        for (int i = 1; i <= 10; i++) {
            System.out.println("Ingrese el número " + i + ":");
            numero = entrada.nextInt();
            suma += numero;
        }
        System.out.println("La suma total es: " + suma);
    }

}
