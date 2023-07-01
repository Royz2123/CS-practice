/**
 * Exercise_3_2 - Find the type of the triangle
 *
 */
public class Exercise_3_2 {

	/**
	 * Finds the type of the triangle
	 *
	 * @param edge1 the length of edge 1.
	 * @param edge2 the length of edge 2.
	 * @param edge3 the length of edge 3.
	 * @return the type of the triangle.
	 */
	public static int findTriangleType(double edge1, double edge2, double edge3) {
		if (edge1 <= 0 || edge2 <= 0 || edge3 <= 0) {
			return -1;
		} else if (edge1 == edge2 && edge2 == edge3) {
			return 1;
		} else if (edge1 != edge2 && edge2 != edge3 && edge1 != edge3) {
			return 3;
		} else {
			return 2;
		}
	}

	public static void main(String[] args) {
		// Run your solution here
	}

}