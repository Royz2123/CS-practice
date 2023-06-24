/**
 * Test exercise template, using the test framework defined below
 * 
 */
public class TestExercise_2_1 {

	public static void main(String[] args) {
		// Creating testing framework
		TestingFramework testFramework = new TestingFramework();

		// Run some tests
        double squareEdgeLength = 4.0;
        double expectedArea = 25.12;
        double actualArea = Exercise_2_1.enclosingCircleArea(squareEdgeLength);
        testFramework.assertEquals(expectedArea, actualArea, "Edge Length = 4");
        
        double squareEdgeLength2 = 1000.0;
        double expectedArea2 = 1570000.0;
        double actualArea2 = Exercise_2_1.enclosingCircleArea(squareEdgeLength2);
        testFramework.assertEquals(expectedArea2, actualArea2, "Edge Length = 1000");
        
        // Print the results back
        testFramework.printTestResults();
	}

}