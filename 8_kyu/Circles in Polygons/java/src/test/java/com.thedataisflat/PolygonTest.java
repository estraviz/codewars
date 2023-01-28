package main.java.com.thedataisflat;

import static org.junit.Assert.*;

import org.junit.Test;

public class PolygonTest {

    @Test
    public void testPolygonCircleDiameter() {

        Polygon polygon = new Polygon();

        polygon.setPoint(4, 5);
        assertEquals(polygon.circleDiameter(), 5.000);

        polygon.setPoint(8, 9);
        assertEquals(polygon.circleDiameter(), 21.728);

        polygon.setPoint(3, 4);
        assertEquals(polygon.circleDiameter(), 2.309);
    }
}