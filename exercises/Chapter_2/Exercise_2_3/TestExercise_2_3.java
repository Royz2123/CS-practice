/**
 * Test Exercise_2_3, using the test framework
 * 
 */
public class TestExercise_2_3 {

	public static void main(String[] args) {
		// Creating testing framework
		TestingFramework testFramework = new TestingFramework();

		// Run some tests
	    List<String> inputs = Arrays.asList("5", "11");
	    String expectedOutput = "1.803400";
	    testFramework.assertOutput(
    		() -> Exercise_2_3.convertToMeters(),
    		expectedOutput, 
    		inputs,
    		false,
    		true, 
    		"5ft 11"
    	);
        
        // Print the results back
        testFramework.printTestResults();
	}

}
