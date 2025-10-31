// 9.5 Herencia parte 5: Presentamos la tarea de hoy Crear la clase Cliente
package domain;

import java.util.Date;

public class Cliente extends Persona {

    private int idCliente;
    private Date fechaRegistro;
    private static int contadorClientes;
    private boolean vip;

    public Cliente(String nombre, char genero, int edad, String direccion, Date fechaRegistro, boolean vip) {
        super(nombre, genero, edad, direccion);
        this.idCliente = ++Cliente.contadorClientes;
        this.fechaRegistro = fechaRegistro;
        this.vip = vip;
    }

    public int getIdCliente() {
        return this.idCliente;
    }

    public Date getFechaRegistro() {
        return this.fechaRegistro;
    }

    public void setFechaRegistro(Date fechaRegistro) {
        this.fechaRegistro = fechaRegistro;
    }

    public boolean isVip() {
        return this.vip;
    }

    public void setVip(boolean vip) {
        this.vip = vip;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Cliente { ");
        sb.append("idCliente: ").append(idCliente);
        sb.append(", Nombre: ").append(super.toString());
        sb.append(", fechaRegistro: ").append(fechaRegistro);
        sb.append(", vip: ").append(vip);
        sb.append(", ").append(super.toString());
        sb.append(" }");
        return sb.toString();
    }
}
