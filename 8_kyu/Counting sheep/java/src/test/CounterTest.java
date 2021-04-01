import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotEquals;


public class CounterTest {
    static Boolean[] array1 = {true,  true,  true,  false,
            true,  true,  true,  true ,
            true,  false, true,  false,
            true,  false, false, true ,
            true,  true,  true,  true ,
            false, false, true,  true };

    static Boolean[] array2 = new Boolean[605];

    static Boolean[] array3 = new Boolean[605];

    static {
        int index = 0;
        for (; index < 500; index++)
            array2[index] = true;
        for (; index < 5; index++)
            array2[index] = null;
        for (; index < 100; index++)
            array2[index] = false;

        index = 0;
        for (; index < 505; index++)
            array3[index] = null;
        for (; index < 100; index++)
            array3[index] = false;
    }

    @Test
    public void test1() {
        assertEquals("There are 17 sheeps in total", 17, new Counter().countSheeps(array1));
    }

    @Test
    public void test2() {
        assertEquals("There are 500 sheeps in total", 500, new Counter().countSheeps(array2));
    }

    @Test
    public void test3() {
        assertEquals("There are 0 sheeps in total", 0, new Counter().countSheeps(array3));
    }

    @Test
    public void test4() {
        assertNotEquals("There are 0 sheeps in total", 0, new Counter().countSheeps(array1));
    }
}