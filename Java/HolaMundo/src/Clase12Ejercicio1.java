import java.util.Scanner;

public class Clase12Ejercicio1 {
    public static void main(String[] args) {
        int totalHoras;
        int semanas;
        int dias;
        int horasFinales;
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el total de horas: ");
        totalHoras = scanner.nextInt();

        semanas = totalHoras / 168;
        int horasRestantes = totalHoras % 168;

        dias = horasRestantes / 24;
        horasFinales = horasRestantes % 24;

        System.out.println(semanas + " semanas, " + dias + " días y " + horasFinales + " horas.");
    }
}

