//Clase08

public class Clase08 {

    public static void main(String[] args) {
        //Operadores unarios: cambio de signos
        var varA = 7;
        var varB = -varA;
        System.out.println("varA = " + varA);
        System.out.println("varB = " + varB);//El resultado sera un numero negativo

        //Operador de negacion
        var varC = true;//Esta literal por default en java es de tipo ooleam
        var varD = !varC;//Aqui esta invirtiendo el valor
        System.out.println("varC = " + varC);
        System.out.println("varD = " + varD);

        //Operadores  unarios de incremento: preincremento
        var varE = 9;//Se va a modificar su valor
        var varF = ++varE;//Simbolo antes de la variable
        //Primero se incrementa la variable y despues se usa su valor
        System.out.println("varE = " + varE);//Se incrementa en la unidad
        System.out.println("varF = " + varF);//Va a sumar uno

        //Postincremento (el simbolo va despues de la variable
        var varG = 3;
        var varH = varG++;//Primero el valor de la variable, luego el incremento
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);

        //Operadoes uarios de decremento
        var varI = 4;
        var varJ = --varI;
        System.out.println("varI = " + varI);//La variabe ya esta con decremento
        System.out.println("varJ = " + varJ);

        //Postdecremento
        var varK = 8;
        var varL = varK--;//Primero el valor de la variable, luego queda el decremento
        System.out.println("varK = " + varK);//Aqui va a decrementar en 1
        System.out.println("varL = " + varL);
        
         
        // OPeradores de Igualdad y Relacionales
        var aNum = 5;
        var bNum = 4;
        var cNum = (aNum == bNum);
        System.out.println("cNum = " + cNum);
        
        var dNum = aNum != bNum;
        System.out.println("dNum = " + dNum);
        
        var cadenaA = "Hello";
        var cadenaB = "bye bye";
        var cVar = cadenaA == cadenaB;
        System.out.println("cVar = " + cVar);  
        
        var fVar = cadenaA.equals(cadenaB);
        System.out.println("fVar = " + fVar);
        
        var gVar = aNum >= bNum;
        System.out.println("gVar = " + gVar);
        
        if (aNum % 2 == 0) {
            System.out.println("El numero es par");
        }
        else {
            System.out.println("El numero es impar");
        }

        var edad = 30;
        var adulto = 18;
        if (edad >= adulto) {
            System.out.println("Es mayor de edad");
        }
        else {
            System.out.println("Es menor de edad");
        }
        
        // Operadores Condicionales
        
        var valorA = 7;
        var valorMinimo = 0;
        var valorMaximo = 10;
        var respuesta = valorA >= 0 && valorA <= 10;
        System.out.println("respuesta: " + respuesta);
        
        if (respuesta) {
            System.out.println("Esta dentro del rango");
        }
        else {
            System.out.println("Esta fuera del rango");
        }

        var vacaciones = false;
        var diaLibre = false;
        if (vacaciones || diaLibre) {
            System.out.println("Puede asistir al juego");
        }
        else {
            System.out.println("No puede asistir al juego");
        }
       
        // Operador ternario
        var resultadoT = (5 > 4) ? "Verdadero" : "Falso";
        System.out.println("resultadoT = " + resultadoT);
     
        var numeroT = 7;
        resultadoT = (numeroT % 2 == 0) ? "Es par" : "Es impar";
        System.out.println("resultadoT = " + resultadoT);
        
        // Prioridad de los operadodres
        var x = 5;
        var y = 10;
        var z = ++x + y--;
        System.out.println("z = " + z);
    }
    
}
