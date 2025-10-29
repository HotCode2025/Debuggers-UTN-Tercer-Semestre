/*
Ejercicio 10: Pedir 10 números y escribir la suma 
total
Hacerlo con la clase Scanner y JOptionPane
 */
package ciclos10;

import javax.swing.JOptionPane;

public class EjercicioCiclos10 {

    public static void main(String[] args) {
        int suma = 0;
        int numero;
        for (int i = 1; i <= 10; i++) {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el numero " + i + ":"));
            suma += numero;
        }
        JOptionPane.showMessageDialog(null, "La suma total es: " + suma);
    }
}
