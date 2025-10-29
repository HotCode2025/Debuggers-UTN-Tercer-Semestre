package ciclos12;

import javax.swing.JOptionPane;

public class Ciclos12 {

    public static void main(String[] args) {
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero para poder calcular su factorial: "));
        long factorial = 1;

        for (int i = 1; i <= numero; i++) {
            factorial *= i;
        }
        JOptionPane.showMessageDialog(null, "El factorial de " + numero + " es: " + factorial);
    }
}
