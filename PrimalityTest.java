public class PrimalityTest {
    public static void main(String[] args) {
        int x = 567;
        int i;
        int check = 0;
        double squareRoot = Math.pow(x, 0.5);
        for (i = 2; i <= squareRoot + 1; i++) {
            if (x % i == 0) {
                System.out.println("Число не простое");
                check = 1;
                break;
            }
        }
        if (check == 0) {
            System.out.println("Число простое");
        }
    }
}
