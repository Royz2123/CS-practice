import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


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
     * Compares the expected and actual integer values.
     *
     * Double is called before the Object assertEquals so it converts them (unwantedly),
     * so I just created another method for ints as well
     *
     * @param expected the expected value
     * @param actual the actual value
     * @param testName the name of the test
     */
    public void assertEquals(int expected, int actual, String testName) {
        if (expected == actual) {
            testResults.add(new TestResult(testName, true, "Got " + actual + " as expected."));
        } else {
            testResults.add(new TestResult(testName, false, "Expected " + expected + ", but got " + actual + "."));
        }
    }

    /**
     * Compares the expected and actual values, and adds a message to the
     * testResults list accordingly.
     *
     * @param expected the expected value
     * @param actual the actual value
     * @param testName the name of the test
     */
    public void assertEquals(int[] expected, int[] actual, String testName) {
        boolean equals = true;
        if (expected == null || actual == null || expected.length != actual.length) {
            equals = false;
        } else {
            for (int i = 0; i < expected.length; i++) {
                if (expected[i] != actual[i]) {
                    equals = false;
                }
            }
        }

        if (equals) {
            testResults.add(new TestResult(testName, true, "Got " + Arrays.toString(actual) + " as expected."));
        } else {
            testResults.add(new TestResult(testName, false, "Expected " + Arrays.toString(expected) + ", but got " + Arrays.toString(actual) + "."));
        }
    }

//     public static <T> boolean assertEquals(T[] expected, T[] actual, String testName) {
//         boolean equals = Arrays.equals(expected, actual);
//         if (equals) {
//             testResults.add(new TestResult(testName, true, "Got " + Arrays.toString(actual) + " as expected."));
//         } else {
//             testResults.add(new TestResult(testName, false, "Expected " + Arrays.toString(expected) + ", but got " + Arrays.toString(actual) + "."));
//         }
//     }

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

