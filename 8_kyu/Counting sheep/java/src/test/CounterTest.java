import org.junit.Test;

import static org.junit.Assert.*;


public class CounterTest {
    Boolean[] array1 = {true,  true,  true,  false,
            true,  true,  true,  true ,
            true,  false, true,  false,
            true,  false, false, true ,
            true,  true,  true,  true ,
            false, false, true,  true };

    @Test
    public void test() {
        assertEquals("There are 17 sheeps in total", 17, new Counter().countSheeps(array1));
        assertNotEquals("There are not 18 sheeps in total", 18, new Counter().countSheeps(array1));
    }
}
