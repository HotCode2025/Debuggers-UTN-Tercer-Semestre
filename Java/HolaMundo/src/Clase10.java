import java.util.Scanner;

public class Clase10 {
    public static void main(String[] args) {
        var condicion = true;
        if (condicion) {
            System.out.println("Condicion Verdadera");
        }
        else {
            System.out.println("Condicion Falsa");
        }

        // Utilizamos la sentencia if-else
        var numero = 5;
        var numeroTexto = "Numero desconocido";
        if (numero == 1) {
            numeroTexto = "Número uno";
        }
        else if (numero == 2) {
            numeroTexto = "Número dos";
        }
        else if (numero == 3) {
            numeroTexto = "Número tres";
        }
        else if (numero == 4) {
            numeroTexto = "Número cuatro";
        }
        System.out.println("numeroTexto = " + numeroTexto);

        
        // Uitilizamos la sentencia switch
        Scanner entrada = new Scanner(System.in);
        System.out.print("Digite un numero entre 1 y 4: ");
        var numero1 = Integer.parseInt(entrada.nextLine());
        var numeroTexto1 = "Numero desconocido";
        switch (numero1) {
            case 1:
                numeroTexto1 = "Número uno";
                break;
            case 2:
                numeroTexto1 = "Número dos";
                break;
            case 3:
                numeroTexto1 = "Número tres";
                break;
            case 4:
                numeroTexto1 = "Número cuatro";
                break;
            default:
                break;
        }
        System.out.println("numeroTexto1 = " + numeroTexto1);
    }
}
