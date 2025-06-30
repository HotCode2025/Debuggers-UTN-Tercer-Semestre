import java.util.Scanner;

public class Clase12Ejercicio2 {
    public static void main(String[] args) {
        double a, b, resultado, aCuadrado, bCuadrado, dosXaXb;
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el valor de a: ");
        a = scanner.nextDouble();

        System.out.print("Ingrese el valor de b: ");
        b = scanner.nextDouble();

        aCuadrado = Math.pow(a, 2);
        bCuadrado = Math.pow(b, 2);
        dosXaXb = 2 * a * b;
        resultado = aCuadrado + bCuadrado + dosXaXb;

        double resultadoDirecto = Math.pow(a + b, 2);

        System.out.println("");
        System.out.println("El resultado de (a+b)^2 es: " + resultado);
        System.out.println("-------------------------------------------------------");
        System.out.println("Verificación: (a+b)^2 calculado directamente es: " + resultadoDirecto);
    }
}
