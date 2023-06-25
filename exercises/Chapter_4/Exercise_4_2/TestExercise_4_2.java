import java.util.Arrays;

/**
 * Test Exercise_4_2, using the test framework
 * 
 */
public class TestExercise_4_2 {

	public static void main(String[] args) {
		// Creating testing framework
		TestingFramework testFramework = new TestingFramework();

		// Run some tests
        Exercise_4_2 s1 = new Exercise_4_2('a');
	    testFramework.assertOutput(
    		() -> s1.lineH(5), 
    		"aaaaa", 
    		Arrays.asList(),
    		true,
    		false, 
    		"5 horizontal a's"
    	);
	    
        Exercise_4_2 s2 = new Exercise_4_2('*');
	    testFramework.assertOutput(
    		() -> s2.lineH(8), 
    		"********", 
    		Arrays.asList(),
    		true,
    		false, 
    		"8 horizontal *'s"
    	);
	    
	    testFramework.assertOutput(
    		() -> s2.lineV(4), 
    		"*\n*\n*\n*\n", 
    		Arrays.asList(),
    		true,
    		false, 
    		"4 vertical *'s"
    	);
	    
	    testFramework.assertOutput(
    		() -> s2.lineDown(5), 
    		"*\n *\n  *\n   *\n    *\n", 
    		Arrays.asList(),
    		true,
    		false, 
    		"Line down of 5 *'s"
    	);
	    
	    testFramework.assertOutput(
    		() -> s2.lineUp(5), 
    		"    *\n   *\n  *\n *\n*\n", 
    		Arrays.asList(),
    		true,
    		false, 
    		"Line up of 5 *'s"
    	);
	    
	    testFramework.assertOutput(
    		() -> s2.fullRect(4, 3), 
    		"****\n****\n****\n", 
    		Arrays.asList(),
    		true,
    		false, 
    		"Rectangle of 3 by 4 *'s"
    	);
	    
	    testFramework.assertOutput(
    		() -> s2.rect(3, 4), 
    		"***\n* *\n* *\n***\n", 
    		Arrays.asList(),
    		true,
    		false, 
    		"Hollow rectangle of 4 by 3 *'s"
    	);
		    
	    
        // Print the results back
        testFramework.printTestResults();
	}
}