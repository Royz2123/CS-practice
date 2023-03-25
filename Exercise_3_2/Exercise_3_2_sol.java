/**
 * Exercise 3.2 - Find if rook and bishop threaten each other
 *
 */
public class Exercise_3_2_sol {

	/**
	 * Determines whether a rook placed at the given row and column is threatening a bishop placed at the given row and column.
	 * A rook threatens a bishop if they are on the same row or column.
	 * 
	 * @param rookRow The row of the rook.
	 * @param rookCol The column of the rook.
	 * @param bishopRow The row of the bishop.
	 * @param bishopCol The column of the bishop.
	 * @return true if the rook threatens the bishop, false otherwise.
	 */
	public static boolean rookIsThreat(int rookRow, int rookCol, int bishopRow, int bishopCol) {
	    // Check if bishop threatens rook horizontally or vertically
	    if (rookRow == bishopRow || rookCol == bishopCol) {
	        return true;
	    }
	    // Otherwise, bishop does not threaten rook
	    return false;
	}

	/**
	 * Determines whether a bishop placed at the given row and column is threatening a rook placed at the given row and column.
	 * A bishop threatens a rook if they are on the same diagonal.
	 * 
	 * @param bishopRow the row of the bishop
	 * @param bishopCol the column of the bishop
	 * @param rookRow the row of the rook
	 * @param rookCol the column of the rook
	 * @return true if the bishop threatens the rook, false otherwise
	 */
	public static boolean bishopIsThreat(int bishopRow, int bishopCol, int rookRow, int rookCol) {
	    int rowDiff = Math.abs(bishopRow - rookRow);
	    int colDiff = Math.abs(bishopCol - rookCol);
	    return rowDiff == colDiff;
	}
	
	public static void main(String[] args) {
		// Set and print rook and bishop positions
		int rookRow = 3;
	    int rookCol = 5;
	    int bishopRow = 6;
	    int bishopCol = 5;
	    System.out.println("The rook is at (3, 5) and the bishop is at (6, 5)");
	    
	    // Find and print threatening status
	    boolean rookIsThreat = rookIsThreat(rookRow, rookCol, bishopRow, bishopCol);
	    boolean bishopIsThreat = bishopIsThreat(rookRow, rookCol, bishopRow, bishopCol);
	    
	    if (rookIsThreat) {
	        System.out.println("The rook threatens the bishop.");
	    } else {
	        System.out.println("The rook does not threaten the bishop.");
	    }
	    if (bishopIsThreat) {
	        System.out.println("The bishop threatens the rook.");
	    } else {
	        System.out.println("The bishop does not threaten the rook.");
	    }
	}
}