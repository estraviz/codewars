import java.math.BigDecimal;
import java.math.RoundingMode;

public class Converter {

    public static final double IMP_GALLON_IN_LITRES = 4.54609188;
    public static final double MILE_IN_KMS = 1.609344;

    public static float mpgToKPM(final float mpg) {

        double kpl = (mpg / IMP_GALLON_IN_LITRES) * MILE_IN_KMS;

        BigDecimal bd = new BigDecimal(kpl).setScale(2, RoundingMode.HALF_UP);
        return bd.floatValue();
    }
}