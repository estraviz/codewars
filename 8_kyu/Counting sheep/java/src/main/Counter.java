// Counting sheep...

import java.util.*;


public class Counter {
    public int countSheeps(Boolean[] arrayOfSheeps) {
        return Collections.frequency(Arrays.asList(arrayOfSheeps), true);
    }
}
