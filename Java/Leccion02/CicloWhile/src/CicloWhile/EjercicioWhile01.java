
package CicloWhile;


public class EjercicioWhile01 {
    public static void main(String[] args) {
        var conteo = 0; // Inferencia de tipos
        while (conteo < 7){
            System.out.println("conteo = " + conteo);
            conteo++; //Vamos aumentando en uno la variable
        }
        
        //Ciclo do while
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador < 7);
        
        //Ciclo for
        //1-declarar variable;2-condicion;3-incremento o decremento
        for(var contando = 0; contando < 7; contando++){
            System.out.println("contando = " + contando);
        }
    }
}
