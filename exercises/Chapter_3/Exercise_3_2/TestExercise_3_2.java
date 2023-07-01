/**
 * Test Exercise_3_2, using the test framework
 */
public class TestExercise_3_2 {

    public static void main(String[] args) {
        // Creating testing framework
        TestingFramework testFramework = new TestingFramework();

        // Run some tests
        testFramework.assertEquals(
                2,
                Exercise_3_2.findTriangleType(3.5, 2.5, 3.5),
                "3.5, 2.5, 3.5 is isosceles"
        );

        testFramework.assertEquals(
                1,
                Exercise_3_2.findTriangleType(1, 1, 1),
                "3.5, 2.5, 3.5 is equilateral"
        );
        testFramework.assertEquals(
                3,
                Exercise_3_2.findTriangleType(1, 2, 3),
                "1, 2, 3 is scalene"
        );
        testFramework.assertEquals(
                -1,
                Exercise_3_2.findTriangleType(-1, -1, -1),
                "-1, -1, -1 is an invalid triangle"
        );
        testFramework.assertEquals(
                -1,
                Exercise_3_2.findTriangleType(0, 2, 2),
                "0, 2, 2 is an invalid triangle"
        );

        // Print the results back
        testFramework.printTestResults();
    }
}