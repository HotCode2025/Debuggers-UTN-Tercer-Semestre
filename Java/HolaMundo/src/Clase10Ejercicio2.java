
import java.util.Scanner;

public class Clase10Ejercicio2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("Digite un número de mes del año: ");
        var mes = Integer.parseInt(entrada.nextLine());
        var estacion = "estacion desconocida";
        switch (mes) {
            case 1: case 2: case 3:
                estacion = "Verano";
                break;
            case 4: case 5: case 6:
                estacion = "Otoño";
                break;
            case 7: case 8: case 9:
                estacion = "Invierno";
                break;
            case 10: case 11: case 12:
                estacion = "Primavera";
                break;
        }

        System.out.println("Estacion = " + estacion);

    }
    
}