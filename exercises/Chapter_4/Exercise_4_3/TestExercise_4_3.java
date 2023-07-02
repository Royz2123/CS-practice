/**
 * Test Exercise_4_3, using the test framework
 * 
 */
public class TestExercise_4_3 {

	public static void main(String[] args) {
		// Creating testing framework
		TestingFramework testFramework = new TestingFramework();

		// Run some tests
        testFramework.assertEquals(true, Exercise_4_3.doesPatternExist("ACTG", "AC"), "AC appears in ACTG");
        testFramework.assertEquals(false, Exercise_4_3.doesPatternExist("ACTG", "AG"), "AG doesn't appear in ACTG");
        testFramework.assertEquals(true, Exercise_4_3.doesPatternExist("ACTGAGT", "CTGA"), "CTGA appears in ACTGAGT");
        testFramework.assertEquals(false, Exercise_4_3.doesPatternExist("", "A"), "Empty genome");
        testFramework.assertEquals(false, Exercise_4_3.doesPatternExist("ACTG", "ACTGACTG"), "pattern larger than genome");
        testFramework.assertEquals(true, Exercise_4_3.doesPatternExist("ACTG", ""), "Empty pattern");

		testFramework.assertEquals(
				true,
				Exercise_4_3.doesPatternAlmostExist("ACTG", "AC", 1),
				"AC appears fully in ACTG (1 mismatch allowed)"
		);
		testFramework.assertEquals(
				true,
				Exercise_4_3.doesPatternAlmostExist("ACTG", "CG", 1),
				"CG has 1 mismatch in ACTG (1 mismatch allowed)"
		);
		testFramework.assertEquals(
				false,
				Exercise_4_3.doesPatternAlmostExist("ACTT", "GG", 1),
				"GG has 2 mismatches in ACTT (1 mismatch allowed)"
		);
		testFramework.assertEquals(
				true,
				Exercise_4_3.doesPatternAlmostExist("ACTT", "GG", 2),
				"GG has 2 mismatches in ACTT (1 mismatches allowed)"
		);
		testFramework.assertEquals(
				true,
				Exercise_4_3.doesPatternAlmostExist("ACTGAGT", "CTGA", 0),
				"CTGA appears in ACTGAGT (0 mismatches allowed)"
		);

		// Print the results back
        testFramework.printTestResults();
	}
}