import java.util.Scanner;

public class Clase11Ejercicio1 {
    public static void main(String[] args) {
        double nota1, nota2, nota3;
        double promedio;
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite la primera nota: ");
        nota1 = scanner.nextDouble();

        System.out.print("Digite la segunda nota: ");
        nota2 = scanner.nextDouble();

        System.out.print("Digite la tercera nota: ");
        nota3 = scanner.nextDouble();

        promedio = (nota1 + nota2 + nota3) / 3;

        if (promedio >= 70) {
            System.out.println("El alumno está aprobado con: " + promedio);
        } 
        else {
            System.out.println("El alumno está desaprobado con: " + promedio);
        }
    }
}
