public class CircleEnclosingSquare {

    public static final double PI = 3.14159265358979323846;

    public static double circleArea(double sideLength) {
        // חישוב רדיוס המעגל על ידי חלוקה של אורך הדיאגונל של הריבוע ב-2
        double radius = sideLength * Math.sqrt(2) / 2;
        // חישוב שטח המעגל באמצעות הנוסחה π * r^2
        double area = PI * Math.pow(radius, 2);
        return area;
    }

    public static void main(String[] args) {
        double sideLength = 4.0;
        System.out.println("שטח המעגל המקיף את הריבוע עם אורך הצד של " + sideLength + ": " + circleArea(sideLength));
    }
}
