/* 4.7 Ejercicio con Ciclos 7 Con la Clase Scanner y JOptionPane
Ejercicio 7: pedir números hasta que se introduzca uno negativo
Calcular la media
 */
package Ciclos07;

import javax.swing.JOptionPane;

public class Ejercicio7 {

    public static void main(String[] args) {
        int numero, suma = 0, contador = 0;

        String entrada = JOptionPane.showInputDialog("Ingresar un número (número negativo para fin): ");
        numero = Integer.parseInt(entrada);

        while (numero >= 0) {
            suma += numero;
            contador++;
            entrada = JOptionPane.showInputDialog("Ingresar un número (número negativo para fin): ");
            numero = Integer.parseInt(entrada);
        }

        if (contador > 0) {
            double media = (double) suma / contador;
            System.out.println("La media de los números ingresados es: " + media);
        }
    }
}
