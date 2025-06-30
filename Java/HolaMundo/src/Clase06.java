
import java.util.Scanner;

//Clase06
public class Clase06 {
    
    public static void main(String[] args) {

        //Tipos primitivos tipo booleanos
        boolean varBool = true;
        System.out.println("varBool = " + varBool);
        
        if (varBool) {
            System.out.println("La bandera es verde");
        } else {
            System.out.println("La bandera es roja");
        }

        //Conversion de tipos primitivos
        //var edad = "20";
        //System.out.println("edad = " + (edad + 1));
        //var valorPI = Double.parseDouble("3.1416");
        //System.out.println("valorPI = " + valorPI);
        //Pedir un valor
        Scanner entrada = new Scanner(System.in);
        //System.out.println("Digite su edad: ");
        //int edad = Integer.parseInt(entrada.nextLine());
        //System.out.println("edad: " + edad);

        //Conversion de tipos primitivosen java parte2
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "programadores".charAt(12);
        System.out.println("fraseChar = " + fraseChar);
        
        System.out.println("Digite un caracter: ");
        fraseChar = entrada.nextLine().charAt(4);
        System.out.println("fraseChar = " + fraseChar);
        
    }
    
}
