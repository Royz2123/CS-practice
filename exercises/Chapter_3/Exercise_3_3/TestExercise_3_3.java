/**
 * Test Exercise_3_3, using the test framework
 * 
 */
public class TestExercise_3_3 {

	public static void main(String[] args) {
		// Creating testing framework
		TestingFramework testFramework = new TestingFramework();

		// Run some tests
	    int rookRow = 3;
	    int rookCol = 5;
	    int bishopRow = 6;
	    int bishopCol = 5;
	    boolean isThreat = Exercise_3_3.rookIsThreat(rookRow, rookCol, bishopRow, bishopCol);
        testFramework.assertEquals(true, isThreat, "Rook (3, 5) threatens bishop (6, 5)");
        
	    int rookRow2 = 8;
	    int rookCol2 = 1;
	    int bishopRow2 = 8;
	    int bishopCol2 = 5;
	    boolean isThreat2 = Exercise_3_3.rookIsThreat(rookRow2, rookCol2, bishopRow2, bishopCol2);
        testFramework.assertEquals(true, isThreat2, "Rook (8, 1) threatens bishop (8, 5)");
        
	    int rookRow3 = 1;
	    int rookCol3 = 1;
	    int bishopRow3 = 8;
	    int bishopCol3 = 5;
	    boolean isThreat3 = Exercise_3_3.rookIsThreat(rookRow3, rookCol3, bishopRow3, bishopCol3);
        testFramework.assertEquals(false, isThreat3, "Rook (1, 1) doesn't threaten bishop (8, 5)");
        
        int rookRow4 = 3;
	    int rookCol4 = 3;
	    int bishopRow4 = 5;
	    int bishopCol4 = 5;
	    boolean isThreat4 = Exercise_3_3.bishopIsThreat(rookRow4, rookCol4, bishopRow4, bishopCol4);
        testFramework.assertEquals(true, isThreat4, "Bishop (5, 5) threatens rook (3, 3)");
        
	    int rookRow5 = 8;
	    int rookCol5 = 1;
	    int bishopRow5 = 1;
	    int bishopCol5 = 8;
	    boolean isThreat5 = Exercise_3_3.bishopIsThreat(rookRow5, rookCol5, bishopRow5, bishopCol5);
        testFramework.assertEquals(true, isThreat5, "Bishop (1, 8) threatens rook (8, 1)");
        
	    int rookRow6 = 1;
	    int rookCol6 = 3;
	    int bishopRow6 = 1;
	    int bishopCol6 = 1;
	    boolean isThreat6 = Exercise_3_3.bishopIsThreat(rookRow6, rookCol6, bishopRow6, bishopCol6);
        testFramework.assertEquals(false, isThreat6, "Bishop (1, 1) doesn't threaten rook (1, 3)");
        
        // Print the results back
        testFramework.printTestResults();
	}
}