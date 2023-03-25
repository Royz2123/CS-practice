/**
 * Exercise 4.2 - Represents a shape made up of a single character.
 *
 */
public class Shape_sol {
    private char tav;

    /**
     * Constructor for the Shape class. Accepts a single char called tav as an attribute.
     * 
     * @param tav The character used to draw the shape.
     */
    public Shape_sol(char tav) {
        this.tav = tav;
    }

    /**
     * Prints a horizontal line of tavs of length len.
     *
     * @param len the length of the line to print
     */
    public void lineH(int len) {
        for (int i = 0; i < len; i++) {
            System.out.print(tav);
        }
        System.out.println();
    }

    /**
     * Prints a vertical line of tavs of length len.
     *
     * @param len the length of the line to print
     */
    public void lineV(int len) {
        for (int i = 0; i < len; i++) {
            System.out.println(tav);
        }
    }

    /**
     * Prints a diagonal line of tavs of length len (main diagonal).
     *
     * @param len the length of the line to print
     */
    public void lineDown(int len) {
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                if (i == j) {
                    System.out.print(tav);
                    System.out.println();
                    break;
                } else {
                    System.out.print(" ");
                }
            }
        }
    }

    /**
     * Prints a diagonal line of tavs of length len (other diagonal).
     *
     * @param len the length of the line to print
     */
    public void lineUp(int len) {
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                if (i + j == len - 1) {
                    System.out.print(tav);
                    System.out.println();
                    break;
                } else {
                    System.out.print(" ");
                }
            }
        }
    }
    
    /**
     * Prints a full rectangle of tavs with the given length and width.
     * 
     * @param l The length of the rectangle to be printed.
     * @param w The width of the rectangle to be printed.
     */
    public void fullRect(int l, int w) {
        for (int i = 0; i < w; i++) {
            for (int j = 0; j < l; j++) {
                System.out.print(tav);
            }
            System.out.println();
        }
    }

    /**
     * Prints a rectangle outline of tavs with the given length and width.
     * 
     * @param l The length of the rectangle to be printed.
     * @param w The width of the rectangle to be printed.
     */
    public void rect(int l, int w) {
        for (int i = 0; i < w; i++) {
            for (int j = 0; j < l; j++) {
                if (i == 0 || i == w - 1 || j == 0 || j == l - 1) {
                    System.out.print(tav);
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
    
    public static void main(String[] args) {
        Shape_sol s = new Shape_sol('*');
        
        s.lineH(5);
        System.out.println();

        s.lineV(5);
        System.out.println();

        s.lineDown(5);
        System.out.println();

        s.lineUp(5);
        System.out.println();

        s.fullRect(3, 4);
        System.out.println();

        s.rect(3, 4);
        System.out.println();
    }
}
