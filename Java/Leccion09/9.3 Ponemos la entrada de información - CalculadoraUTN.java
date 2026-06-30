
import java.util.Scanner;

public class CalculadoraUTN {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("******** Aplicacion Calculadora ********");
        System.out.print("Digite el valor para el operando1: ");
        var opernado1 = Integer.parseInt(entrada.nextLine());
        System.out.print("Digite el valor para el operando2: ");
        var opernado2 = Integer.parseInt(entrada.nextLine());
        
        var resultado = opernado1 + opernado2;
        System.out.println("Resulato = " + resultado);
    }
}

