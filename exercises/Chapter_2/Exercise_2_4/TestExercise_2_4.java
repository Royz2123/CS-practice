import java.util.Arrays;

/**
 * Test Exercise_2_4, using the test framework
 * 
 */
public class TestExercise_2_4 {

	public static void main(String[] args) {
		// Creating testing framework
		TestingFramework testFramework = new TestingFramework();

		// Create table object
		Exercise_2_4 table1 = new Exercise_2_4("red", 4);

		// Test set & get table color
		table1.setColor("blue");
		testFramework.assertEquals(table1.getColor(), "blue", "Set table color to blue");

		// Test set & get numDiners
		table1.setNumDiners(6);
		testFramework.assertEquals(table1.getNumDiners(), 6, "Set table numDiners to 6");

		// Test toString
		Exercise_2_4 table2 = new Exercise_2_4("red", 4);
		testFramework.assertOutput(
    		() -> System.out.println(table2.toString()),
    		"red",
    		Arrays.asList(),
    		true,
    		true,
    		"toString method contains color"
    	);
		testFramework.assertOutput(
			() -> System.out.println(table2.toString()),
			"4",
			Arrays.asList(),
			true,
			true,
			"toString method contains numDiners"
		);

		// Test num of full tables
		testFramework.assertEquals(table2.numOfFullTables(6), 1, "Full tables for numDiners=4, n=6");
		testFramework.assertEquals(table2.numOfFullTables(12), 3, "Full tables for numDiners=4, n=12");
		testFramework.assertEquals(table2.numOfFullTables(0), 0, "Full tables for numDiners=4, n=0");

		// Test left over method
		testFramework.assertEquals(table2.leftOver(6), 2, "Left over for numDiners=4, n=6");
		testFramework.assertEquals(table2.leftOver(12), 0, "Left over for numDiners=4, n=12");
		testFramework.assertEquals(table2.leftOver(0), 0, "Left over for numDiners=4, n=0");

        // Print the results back
        testFramework.printTestResults();
	}
}