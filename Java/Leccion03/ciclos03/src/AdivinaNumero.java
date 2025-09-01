import java.util.Scanner;
import java.util.Random;

public class AdivinaNumero {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            Random random = new Random();
            
            int numeroSecreto = random.nextInt(101); // Número entre 0 y 100
            int intentos = 0;
            int numeroUsuario = -1;
            
            System.out.println("🔢 ¡Bienvenido al juego de adivinar el número!");
            System.out.println("Estoy pensando en un número entre 0 y 100...");
            
            while (numeroUsuario != numeroSecreto) {
                System.out.print("👉 Ingresá tu número: ");
                numeroUsuario = scanner.nextInt();
                intentos++;
                
                if (numeroUsuario < numeroSecreto) {
                    System.out.println("📈 Es mayor");
                } else if (numeroUsuario > numeroSecreto) {
                    System.out.println("📉 Es menor");
                } else {
                    System.out.println("🎉 ¡Correcto! El número era " + numeroSecreto);
                    System.out.println("🔁 Lo adivinaste en " + intentos + " intentos.");
                }
            }
        }
    }
}
