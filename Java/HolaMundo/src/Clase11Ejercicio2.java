
import java.util.Scanner;

public class Clase11Ejercicio2 {
    public static void main(String[] args) {
        double compra, descuento, precioFinal;
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite la cantidad a pagar: ");
        compra = scanner.nextDouble();

        descuento = 0;
        if (compra > 100) {
            descuento = compra * 0.20;
        }

        precioFinal = compra - descuento;
        System.out.println("El precio a pagar es: " + precioFinal);
    }
}