// Clase1
// 1.2 Ciclo While
package CicloWhile;

public class EjercicioWhile01 {

    public static void main(String[] args) {
        var conteo = 0; // Inferencia de tipos
        while (conteo < 7) {
            System.out.println("conteo = " + conteo);
            conteo++; //Vamos aumentando en uno la variable
        }

        // 1.3 Ciclo do while
        var contador = 0;
        do {
            System.out.println("contador = " + contador);
            contador++;
        } while (contador < 7);

        // 1.4 Ciclo for
        //1-declarar variable;2-condicion;3-incremento o decremento
        for (var contando = 0; contando < 7; contando++) {
            System.out.println("contando = " + contando);
        }

        // 1.5 Palabra reservada break
        for (var contandos = 0; contandos < 7; contandos++) {
            if (contandos % 2 == 0) {
                System.out.println("contandos = " + contandos);
                break;
            }
        }

        //Palabra reservada continue
        for (var num = 0; num < 7; num++) {
            if (num % 2 != 0) {
                continue; //Vamos a la siguiente iteracion
            }
            System.out.println("num = " + num);
        }

        // 1.6 Etiqueta Labels
        inicio:
        for (var etiqueta = 0; etiqueta < 7; etiqueta++) {
            if (etiqueta % 2 != 0) {
                continue inicio;
            }
            System.out.println("etiqueta = " + etiqueta);
        }
    }
}
