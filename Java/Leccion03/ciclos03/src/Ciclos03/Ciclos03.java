package Ciclos03;

import javax.swing.JOptionPane;

public class Ciclos03 {
    public static void main(String[] args) {
        int numero;

        do {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un nÃºmero (0 para terminar):"));

            if (numero != 0) {
                if (numero % 2 == 0) {
                    JOptionPane.showMessageDialog(null, numero + " es PAR");
                } else {
                    JOptionPane.showMessageDialog(null, numero + " es IMPAR");
                }
            }
        } while (numero != 0);

        JOptionPane.showMessageDialog(null, "Programa finalizado.");
    }
}
