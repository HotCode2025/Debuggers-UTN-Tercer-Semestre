// 9.7 Agregamos try catch para las excepciones
            try {
                var operacion = Integer.parseInt(entrada.nextLine());
                if (operacion >= 1 && operacion <= 4){
                    ejecutarOperacion(operacion, entrada);
                } //Fin del if
                else if (operacion == 5) {
                    System.out.println("Hasta pronto...");
                    break;//9.6 Ciclo y su salida con break
                }
                else {
                    System.out.println("Opcion erronea"+operacion);
                }
                //Imprimimos un salto de linea antes de repetir el menu
                System.out.println();//9.6 Ciclo y su salida con break
                // 9.7 Agregamos try catch para las excepciones
            } catch (Exception e){ //Fin try, comienzo del catch
                System.out.println("Ocurrio un error: "+e.getMessage());
                System.out.println();
            }