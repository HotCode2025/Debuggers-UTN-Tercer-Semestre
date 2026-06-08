// 8.4 Creamos nuestra propia excepción -> Parte 1, 2 y 3
// Video02
package aritmetica;

import excepciones.OperacionExepcion;


public class Aritmetica {
    public static int division(int numerador, int denominador) throws OperacionExepcion{
        if(denominador == 0){
            throw new OperacionExepcion("Division entre cero");
        }
        return numerador / denominador;
    }
}
