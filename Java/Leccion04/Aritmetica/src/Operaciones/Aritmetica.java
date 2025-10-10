package Operaciones;

public class Aritmetica {

    //Atributos de la clase
    int a;
    int b;

    //Metodo
    public void sumarNumeros() {
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }

    public int sumarConRetorno() {
        //Int resultado = a + b;
        return this.a + this.b;
    }

    public int sumarConArgumentos(int a, int b) {
        this.a = a;
        this.b = b;
        //return a + b;
        return this.sumarConRetorno();
    }
}
