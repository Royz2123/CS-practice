/**
 * Exercise_2_4_sol - The Table class.
 *
 */
public class Exercise_2_4_sol {
    private String color;
    private int numDiners;

    public Exercise_2_4_sol(String color, int numDiners) {
        this.color = color;
        this.numDiners = numDiners;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public int getNumDiners() {
        return numDiners;
    }

    public void setNumDiners(int numDiners) {
        this.numDiners = numDiners;
    }

    public int tablePrice() {
        return numDiners * 400;
    }

    public String toString() {
        return "Table with color " + color + " and " + numDiners + " diners, price: " + tablePrice() + " ILS.";
    }

    public int numOfFullTables(int n) {
        return n / numDiners;
    }

    public int leftOver(int n) {
        return n % numDiners;
    }

    public static void main(String[] args) {
        // Run your solution here
    }
}
