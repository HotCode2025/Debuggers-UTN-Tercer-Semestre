// 5.5 Clases Abstractas (abstract) Parte 1, 2 y 3
// Video 02
package domain;

public abstract class FiguraGeometrica {

    protected String tipoFigura;

    protected FiguraGeometrica(String tipoFigura) {
        this.tipoFigura = tipoFigura;
    }

    //Metodo abstracto
    public abstract void dibujar();

    //Agregamos el get y set
    public String getTipoFigura() {
        return tipoFigura;
    }

    public void setTipoFigura(String tipoFigura) {
        this.tipoFigura = tipoFigura;
    }

    @Override
    public String toString() {
        return "FigurasGeometricas{" + "tipoFigura=" + tipoFigura + '}';
    }

}
