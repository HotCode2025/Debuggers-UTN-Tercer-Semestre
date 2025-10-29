// 4.6 Creación de Métodos
package Operaciones;

public class Aritmetica {

    //Atributos de la clase
    int a;
    int b;
    
    //6.1 Sobrecarga de métodos
    // El cnstructor es un método especial
    public Aritmetica() {//Constructor 1 vacio
        System.out.println("Se esta ejecutando esta costructor número uno");
    }

    //Estamos viendo lo que se llama sobrecarga de constructores
    public Aritmetica(int a, int b) {//Constructor 2
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando esta costructor número dos");
    }

    //Metodo
    public void sumarNumeros() {
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }

    // 5.2 Clase Aritmética: Creamos un método, recorremos con Debbug
    public int sumarConRetorno() {
        //Int resultado = a + b;
        return this.a + this.b;
    }

    // 5.3 Paso de argumentos a un método
    public int sumarConArgumentos(int a, int b) {
        this.a = a; //El argumento a se asigna al atributo this.a
        this.b = b;
        //return a + b;

        // 5.4 Un método llamando a otro método
        return this.sumarConRetorno();
    }
}
