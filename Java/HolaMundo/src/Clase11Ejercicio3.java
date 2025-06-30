import java.util.Scanner;

public class Clase11Ejercicio3 {
    public static void main(String[] args) {
        double num1, num2, resultado;
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite el primer números: ");
        num1 = scanner.nextDouble();
        System.out.print("Digite el segundo números: ");
        num2 = scanner.nextDouble();

        if (num1 == num2) {
            resultado = num1 * num2;
        } 
        else {
            if (num1 > num2) {
                resultado = num1 - num2;
            } 
            else {
                resultado = num1 + num2;
            }
        }
        System.out.println("El resultado es: " + resultado);
    }
}