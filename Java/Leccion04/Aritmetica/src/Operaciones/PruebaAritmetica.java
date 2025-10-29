package Operaciones;

public class PruebaAritmetica {

    // 5.1 Clase Aritmética: Creamos un objeto
    public static void main(String[] args) {
        //6.2 Alcance de variables
        var a = 10; //variables locales
        //6.3 Engineer Java: Memoria stack y heap, tratamiento de residuos
        int b = 7; //Memoria stack 
        miMetodo();//Llamamos el metodo nuevo
        Aritmetica aritmetica1 = new Aritmetica();
        //Para almacenar un objeto a los atributos se utiliza la memoria heap
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();

        // 5.2 Clase Aritmética: Creamos un método, recorremos con Debbug
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);

        // 5.3 Paso de argumentos a un método
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = " + resultado);

        //6.1 Sobrecarga de métodos
        System.out.println("aritmetica1 a: " + aritmetica1.a);
        System.out.println("aritmetica1 b: " + aritmetica1.b);

        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);
        //aritmetica1 = null; nunca utilizar esto, no se debe hacer
        //System.gc(); metodo para limpiar residuos, es pesado, no utilizar
        Persona persona = new Persona("Jairo", "Ubilla");
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre: " + persona.nombre); //7.1 Uso de la palabra this Parte 1 y crear una clase a continuación de otra
        System.out.println("Perona apellido: " + persona.apellido);//7.1 Uso de la palabra this Parte 1 y crear una clase a continuación de otra
    }

// Modularidad creamos un nuevo método
    public static void miMetodo() {
        //a = 10; //una variable esta limitada
        System.out.println("Aqui hay otro metodo");
    }
}

//7.1 Uso de la palabra this Parte 1 y crear una clase a continuación de otra
// Creamos una nueva clase
class Persona {

    String nombre;
    String apellido;

    Persona(String nombre, String apellido) { //Constructor 
        super();//Lamada al constructor de la clase Padre object
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: " + this);

    }
}
//7.4  Uso de la palabra this Parte 2

class Imprimir {

    public Imprimir() {
        super();//El constructor de la clase padre, para reservar memoria
    }

    public void imprimir(Persona persona) {
        System.out.println("Persona desde la clase imprimir: " + persona);
        System.out.println("Impresion del objeto actual (this): " + this);
    }
}
