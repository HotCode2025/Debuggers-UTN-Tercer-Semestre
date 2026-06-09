// 7.5 Pruebas: Parte 1 
package test;

import accesodatos.*;

public class TestInterfaces {

    public static void main(String[] args) {
        IAccesoDatos datos = new ImplementacionMySql();
        datos.listar();
        