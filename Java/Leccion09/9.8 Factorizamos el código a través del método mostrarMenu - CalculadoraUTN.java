import java.util.Scanner;

public class CalculadoraUTN {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        while (true) { // ciclo infinito
            System.out.println("******** Aplicacion Calculadora ********");
            mostrarMenu();
            try {
                var operacion = Integer.parseInt(entrada.nextLine());
                if (operacion >= 1 && operacion <= 4) {
                    System.out.print("Digite el valor para el operando1: ");
                    var operando1 = Integer.parseInt(entrada.nextLine());
                    System.out.print("Digite el valor para el operando2: ");
                    var operando2 = Integer.parseInt(entrada.nextLine());

                    int resultado;
                    switch (operacion) {
                        case 1 -> { // Suma
                            resultado = operando1 + operando2;
                            System.out.println("Resultado de la suma: " + resultado);
                        }
                        case 2 -> { // Resta
                            resultado = operando1 - operando2;
                            System.out.println("Resultado de la resta: " + resultado);
                        }
                        case 3 -> { // Multiplicación
                            resultado = operando1 * operando2;
                            System.out.println("Resultado de la multiplicación: " + resultado);
                        }
                        case 4 -> { // División
                            resultado = operando1 / operando2;
                            System.out.println("Resultado de la división: " + resultado);
                        }
                        default -> System.out.println("Opción erronea: " + operacion);
                    } // Fin switch
                } // Fin del if
                else if (operacion == 5) {
                    System.out.println("Hasta pronto ....");
                    break; // rompe el ciclo y sale
                }
                else {
                    System.out.println("Opcion erronea: " + operacion);
                }
                // Imprimimos un salto de linea
                System.out.println("");
            } catch (Exception e) {
                System.out.println("Ocurrio un error: " + e.getMessage());
                System.out.println("");
            }
        } // Fin while
    } // Fin main
    
    private static void mostrarMenu() {
        // Mostramos el menu
        System.out.println("""
                           1. Suma
                           2. Resta
                           3. Multiplicación
                           4. División
                           5. Salir
                           """);
        System.out.print("Operacion a realizar: ");
    }
} // Fin clase

