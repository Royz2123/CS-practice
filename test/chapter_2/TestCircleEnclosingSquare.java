package chapter_2;

import org.junit.Test;
import org.junit.Assert;


public class TestCircleEnclosingSquare extends TestBase {

    @Test
    public void testCircleArea() {
        double sideLength = 4.0;
        double expectedArea = 25.12;
        double actualArea = CircleEnclosingSquare.circleArea(sideLength);
        Assert.assertEquals(expectedArea, actualArea, double_delta);
    }
}
