/**
 * Test Exercise_5_3, using the test framework
 *
 */
public class TestExercise_5_3 {

	public static void main(String[] args) {
		// Creating testing framework
		TestingFramework testFramework = new TestingFramework();

		// Run some tests
		int arr1[] = {9, 9};
        testFramework.assertEquals(81, Exercise_5_3.calcDigitMultiplication(arr1), "Digits Multiplication in [9, 9]");

		int arr2[] = {6, 10, 23, 2, 56};
        testFramework.assertEquals(12, Exercise_5_3.calcDigitMultiplication(arr2), "Digits Multiplication in [6, 10, 23, 2, 56]");

		int arr3[] = {1, 2, 3, 4, 5};
        testFramework.assertEquals(120, Exercise_5_3.calcDigitMultiplication(arr3), "Digits Multiplication in [1, 2, 3, 4, 5]");

		int arr4[] = {10, 11, 12};
        testFramework.assertEquals(-1, Exercise_5_3.calcDigitMultiplication(arr4), "Digits Multiplication in [10, 11, 12]");

		int arr5[] = {};
        testFramework.assertEquals(-1, Exercise_5_3.calcDigitMultiplication(arr5), "Digits Multiplication in []");

        // Print the results back
        testFramework.printTestResults();
	}
}