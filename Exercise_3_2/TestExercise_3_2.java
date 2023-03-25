import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.List;


/**
 * Test exercise template, using the test framework defined below
 * 
 */
public class TestExercise_3_2 {

	public static void main(String[] args) {
		// Creating testing framework
		TestingFramework testFramework = new TestingFramework();

		// Run some tests
	    int rookRow = 3;
	    int rookCol = 5;
	    int bishopRow = 6;
	    int bishopCol = 5;
	    boolean isThreat = Exercise_3_2_sol.rookIsThreat(rookRow, rookCol, bishopRow, bishopCol);
        testFramework.assertEquals(true, isThreat, "Rook (3, 5) threatens bishop (6, 5)");
        
	    int rookRow2 = 8;
	    int rookCol2 = 1;
	    int bishopRow2 = 8;
	    int bishopCol2 = 5;
	    boolean isThreat2 = Exercise_3_2_sol.rookIsThreat(rookRow2, rookCol2, bishopRow2, bishopCol2);
        testFramework.assertEquals(true, isThreat2, "Rook (8, 1) threatens bishop (8, 5)");
        
	    int rookRow3 = 1;
	    int rookCol3 = 1;
	    int bishopRow3 = 8;
	    int bishopCol3 = 5;
	    boolean isThreat3 = Exercise_3_2_sol.rookIsThreat(rookRow3, rookCol3, bishopRow3, bishopCol3);
        testFramework.assertEquals(false, isThreat3, "Rook (1, 1) doesn't threaten bishop (8, 5)");
        
        int rookRow4 = 3;
	    int rookCol4 = 3;
	    int bishopRow4 = 5;
	    int bishopCol4 = 5;
	    boolean isThreat4 = Exercise_3_2_sol.bishopIsThreat(rookRow4, rookCol4, bishopRow4, bishopCol4);
        testFramework.assertEquals(true, isThreat4, "Bishop (5, 5) threatens rook (3, 3)");
        
	    int rookRow5 = 8;
	    int rookCol5 = 1;
	    int bishopRow5 = 1;
	    int bishopCol5 = 8;
	    boolean isThreat5 = Exercise_3_2_sol.bishopIsThreat(rookRow5, rookCol5, bishopRow5, bishopCol5);
        testFramework.assertEquals(true, isThreat5, "Bishop (1, 8) threatens rook (8, 1)");
        
	    int rookRow6 = 1;
	    int rookCol6 = 3;
	    int bishopRow6 = 1;
	    int bishopCol6 = 1;
	    boolean isThreat6 = Exercise_3_2_sol.bishopIsThreat(rookRow6, rookCol6, bishopRow6, bishopCol6);
        testFramework.assertEquals(false, isThreat6, "Bishop (1, 1) doesn't threaten rook (1, 3)");
        
        // Print the results back
        testFramework.printTestResults();
	}
}



/**
 * Testing framework that stores and displays a series of tests
 *
 */
class TestingFramework {
    private List<TestResult> testResults;

    public TestingFramework() {
        testResults = new ArrayList<>();
    }

    /**
     * Compares the expected and actual values, and adds a message to the
     * testResults list accordingly. If the values being compared are doubles,
     * a margin of error is allowed.
     * 
     * @param expected the expected value
     * @param actual the actual value
     * @param delta the maximum allowed difference for double comparisons
     * @param testName the name of the test
     */
    public void assertEquals(double expected, double actual, double delta, String testName) {
        if (Math.abs(expected - actual) <= delta) {
            testResults.add(new TestResult(testName, true, "Got " + actual + " as expected."));
        } else {
            testResults.add(new TestResult(testName, false, "Expected " + expected + ", but got " + actual + "."));
        }
    }

    /**
     * Compares the expected and actual values, and adds a message to the
     * testResults list accordingly. If the values being compared are doubles,
     * a default margin of error of 0.001 is used.
     * 
     * @param expected the expected value
     * @param actual the actual value
     * @param testName the name of the test
     */
    public void assertEquals(double expected, double actual, String testName) {
        assertEquals(expected, actual, 0.001, testName);
    }

    /**
     * Compares the expected and actual values, and adds a message to the
     * testResults list accordingly.
     * 
     * @param expected the expected value
     * @param actual the actual value
     * @param testName the name of the test
     */
    public void assertEquals(Object expected, Object actual, String testName) {
        if (expected.equals(actual)) {
            testResults.add(new TestResult(testName, true, "Got " + actual + " as expected."));
        } else {
            testResults.add(new TestResult(testName, false, "Expected " + expected + ", but got " + actual + "."));
        }
    }

    
    /**
     * Asserts that the output to the console produced by the given method is equal to the expected output.
     *
     * @param testMethod The method to be tested
     * @param expectedOutput The expected output to the console
     * @param args List of arguments to pass to the runnable if it's waiting for input
     * @param passArgsDirectly are the args passed through the method (or through the standard input)
     * @param containsExpectedOutput should the method check if the method contains the output (or equals)
     * @param testName the name of the test
     */
    public void assertOutput(
    		Runnable testMethod, 
    		String expectedOutput, 
    		List<String> args, 
    		boolean passArgsDirectly,
    		boolean containsExpectedOutput, 
    		String testName
    ) {
	    ByteArrayOutputStream baos = new ByteArrayOutputStream();
	    PrintStream ps = new PrintStream(baos);
	    InputStream oldIn = System.in;
	    PrintStream oldOut = System.out;
	    try {
	        System.setOut(ps);
	        if (passArgsDirectly) {
	        	testMethod.run();
	        } else {
	            ByteArrayInputStream bais = new ByteArrayInputStream(String.join(System.lineSeparator(), args).getBytes());
	            System.setIn(bais);
	            testMethod.run();
	        }
	        System.out.flush();
	        String actualOutput = baos.toString().replaceAll("\\r\\n", "\n");
	        
	        // Escape all newlines for printing
		    expectedOutput = expectedOutput.trim().replaceAll("\n", "\\n");
		    actualOutput = actualOutput.trim().replaceAll("\n", "\\n");
		    
	        // Check if outputs are equal / contain
	        if (containsExpectedOutput) {
	            if (actualOutput.contains(expectedOutput)) {
	                testResults.add(new TestResult(testName, true, "Printed '" + actualOutput + "' which contained '" + expectedOutput + "' as expected."));
	            } else {
	                testResults.add(new TestResult(testName, false, "Expected the method to contain: '" + expectedOutput + "', but instead it printed: '" + actualOutput + "'."));
	            }
	        } else {
	            if (actualOutput.equals(expectedOutput)) {
	                testResults.add(new TestResult(testName, true, "Printed '" + actualOutput + "' as expected."));
	            } else {
	                testResults.add(new TestResult(testName, false, "Expected the method to print: '" + expectedOutput + "', but instead it printed: '" + actualOutput + "'."));
	            }
	        }
	    } finally {
	        System.setOut(oldOut);
	        System.setIn(oldIn);
	    }
    }


    /**
     * Prints the results of the tests, including how many tests passed and failed.
     */
    public void printTestResults() {
        int totalTests = testResults.size();
        int numPassed = 0;
        
        // Print how many test passed successfully
        for (TestResult result : testResults) {
            if (result.passed) {
                numPassed++;
            }
        }
        System.out.println("Tests passed successfully: " + numPassed + "/" + totalTests);

        // Print which tests failed
        for (int i = 0; i < totalTests; i++) {
            System.out.println(formatTestResult(testResults.get(i), i + 1));
        }
    }

    /**
     * Formats the test result for printing.
     * 
     * @param result the test result to format
     * @return the formatted test result as a String
     */
    private String formatTestResult(TestResult result, int testIndex) {
        StringBuilder sb = new StringBuilder();
        
        // Write if test failed 
        sb.append("\t").append("Test ").append(testIndex);
        if (result.passed) {
            sb.append(" passed");
        } else {
            sb.append(" failed");
        }
        
        // Add test name if provided
        if (result.testName != null) {
            sb.append(" (").append(result.testName).append(")");
        }
        
        // Add error message for failed tests if provided
        if (result.errorMessage != null) {
        	sb.append(": ").append(result.errorMessage);
        }

        return sb.toString();
    }

    /**
     * A class to represent the result of a single test.
     */
    private static class TestResult {
        private String testName;
        private boolean passed;
        private String errorMessage;

        public TestResult(String testName, boolean passed) {
            this.testName = testName;
            this.passed = passed;
        }

        public TestResult(String testName, boolean passed, String errorMessage) {
            this.testName = testName;
            this.passed = passed;
            this.errorMessage = errorMessage;
        }
    }
}

