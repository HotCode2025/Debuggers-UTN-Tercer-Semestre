
import java.util.Scanner;

public class Clase12Ejercicio3 {
    public static void main(String[] args) {
        double calificacionParticipacion, calificacionPrimerParcial;
        double calificacionSegundoParcial, calificacionExamenFinal;
        double calificacionFinal;
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese la calificación de Participación (0-100): ");
        calificacionParticipacion = scanner.nextDouble();

        System.out.print("Ingrese la calificación del Primer Examen Parcial (0-100): ");
        calificacionPrimerParcial = scanner.nextDouble();

        System.out.print("Ingrese la calificación del Segundo Examen Parcial (0-100): ");
        calificacionSegundoParcial = scanner.nextDouble();

        System.out.print("Ingrese la calificación del Examen Final (0-100): ");
        calificacionExamenFinal = scanner.nextDouble();

        calificacionFinal = (calificacionParticipacion * .10) + (calificacionPrimerParcial * .25) +
                            (calificacionSegundoParcial * .25) + (calificacionExamenFinal * .40);

        System.out.printf("La CALIFICACIÓN FINAL del estudiante es: %.2f%n", calificacionFinal);
    }
}