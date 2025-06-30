//Clase04

public class Clase04 {

    public static void main(String[] args) {
        byte numEnteroByte = 127;
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor minimo del Byte:" + Byte.MIN_VALUE);
        System.out.println("Valor minimo del Byte:" + Byte.MAX_VALUE);

        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("Valor minimo del Short:" + Short.MIN_VALUE);
        System.out.println("Valor minimo del Short:" + Short.MAX_VALUE);

        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("Valor minimo del Int:" + Integer.MIN_VALUE);
        System.out.println("Valor minimo del Int:" + Integer.MAX_VALUE);

        long numEnteroLong = 9223372036854775807L;
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor minimo del Long:" + Long.MIN_VALUE);
        System.out.println("Valor minimo del Long:" + Long.MAX_VALUE);

        float numFloat = 3.402823E38F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("Valor minimo del float:" + Float.MIN_VALUE);
        System.out.println("Valor minimo del fioat:" + Float.MAX_VALUE);

        double numDouble = 1.7976931348623157E308D;
        System.out.println("numDouble= " + numDouble);
        System.out.println("Valor minimo del double:" + Double.MIN_VALUE);
        System.out.println("Valor minimo del double:" + Double.MAX_VALUE);

    }

}
