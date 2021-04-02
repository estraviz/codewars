import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotEquals;


public class TestKata {

    @Test
    public void exampleTests() {
        assertEquals(new Kata().quarterOf(3), 1);
        assertEquals(new Kata().quarterOf(8), 3);
        assertEquals(new Kata().quarterOf(11), 4);

        assertNotEquals(new Kata().quarterOf(3), 2);
        assertNotEquals(new Kata().quarterOf(8), 4);
        assertNotEquals(new Kata().quarterOf(11), 1);
    }
}
