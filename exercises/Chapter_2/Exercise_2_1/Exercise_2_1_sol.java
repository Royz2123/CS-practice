/**
 * Exercise 2.1 - Find the area of the enclosing circle given an edge length
 *
 */
public class Exercise_2_1_sol {

    /**
     * Compute the enclosing circles' area
     *
     * @param squareEdgeLength the length of any edge in the square
     * @return the enclosing circles' area
     **/
    public static double enclosingCircleArea(double squareEdgeLength) {
    	// Compute the radius by calculating the squares' diagonal 
        double radius = squareEdgeLength * Math.sqrt(2) / 2;
        double pi = 3.14;
        
        // Compute the area using the known circle area formula
        double area = pi * Math.pow(radius, 2);
        return area;    
    }
	
	public static void main(String[] args) {
        double squareEdgeLength = 4.0;
        System.out.println("The area of the circle enclosing a square with edge length " + squareEdgeLength + " is: " + enclosingCircleArea(squareEdgeLength));
	}

}