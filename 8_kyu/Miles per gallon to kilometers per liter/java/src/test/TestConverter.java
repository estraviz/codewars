import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class TestConverter {

    @Test
    public void test1() {
        assertEquals(3.54f, Converter.mpgToKPM(10), 0.001f);
    }

    @Test
    public void test2() {
        assertEquals(7.08f, Converter.mpgToKPM(20), 0.001f);
    }

    @Test
    public void test3() {
        assertEquals(10.62f, Converter.mpgToKPM(30), 0.001f);
    }

    @Test
    public void test4() {
        assertEquals(8.50f, Converter.mpgToKPM(24), 0.001f);
    }

    @Test
    public void test5() {
        assertEquals(12.74f, Converter.mpgToKPM(36), 0.001f);
    }
}