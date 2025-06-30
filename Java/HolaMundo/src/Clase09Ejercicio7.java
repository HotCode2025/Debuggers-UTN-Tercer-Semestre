/*
Clase 9 - Ejercicio 7: Una compañia de autos usados paga a su empleados de ventas un salario de $1000 mensuales
mas un acomision de $150 por cada auto vendido, mas el 5% del valor de venta por auto
Hacer un programa que calcule e imprima el salario mensual de un vendedor dado
El salario de 1000 lo vamos a manejar como un dato constante, para asignarlo debemos usar la palabra rservada "final"

Salario = 1000 + 150 * cantidadVendidos + totalValorVendido * 5 / 100
*/
import java.util.Scanner;

public class Clase09Ejercicio7 {
    public static void main(String[] args) {
        final double SALARIO_BASE = 1000; // Salario mensual $1000
        final double COMISION_POR_AUTO = 150; // Comisión por auto vendido $150
        final double PORCENTAJE_VENTA = 0.05; // 5% del valor de cada auto vendido

        Scanner scanner = new Scanner(System.in);

        // Pido la cantidad de autos vendidos
        System.out.print("Ingrese la cantidad de autos vendidos: ");
        int autosVendidos = scanner.nextInt();

        double totalVenta = 0;

        // Pido el precio de cada auto vendido
        for (int i = 0; i < autosVendidos; i++) {
            System.out.print("Ingrese el precio del auto " + (i + 1) + ": ");
            double precioAuto = scanner.nextDouble();
            totalVenta += precioAuto * PORCENTAJE_VENTA;
        }

        // Calcular salario total
        double salarioTotal = SALARIO_BASE + (autosVendidos * COMISION_POR_AUTO) + totalVenta;
        System.out.println("El salario mensual del vendedor es: $" + salarioTotal);

        scanner.close();
    }
}

