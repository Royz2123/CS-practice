package chapter_2;

import org.junit.Test;
import org.junit.Assert;

public class TestMetersConverter extends TestBase {

    @Test
    public void testConvertToMeters() {
        double feet = 5.0;
        double inches = 11.0;
        double expectedMeters = 1.8034;
        double actualMeters = MetersConverter.convertToMeters(feet, inches);
        Assert.assertEquals(expectedMeters, actualMeters, double_delta);
    }
}