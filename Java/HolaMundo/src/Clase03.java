
import java.util.Scanner;


public class Clase03 {

    public static void main(String[] args) {
        //----------------------------------------------------
        //Reglas para definir una variable en Java

        var usuario = "Osvaldo";
        var titulo = "Ingeniero";
        var union = titulo + " " + usuario;
        System.out.println("union = " + union);

        //----------------------------------------------------
        var a = 8;
        var b = 4;
        System.out.println(usuario + (a + b));

        //-----------------------------------------------------
        //Ejercicio: Caracteres Especiales con Java
        var nombre = "Natalia";
        System.out.println("Nueva linea: \n" + nombre);//Diagonal inversa y letra n
        System.out.println("Tabulador: \t" + nombre);//Tabulador un espacio para centrar
        System.out.println(" \t.:MENU:.");
        System.out.println("Retroseso: \b" + nombre);//Caracter de Retroseso
        System.out.println("Comillas simples: \'" + nombre + "\'");
        System.out.println("Comillas Dobles: \"" + nombre + "\"");
        
        //-----------------------------------------------------------
        
        //Clase Scaner
        
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escrba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: "+titulo2+" "+usuario2);
        
        
               
    }
}
