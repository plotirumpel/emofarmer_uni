public class IntroTaskCat {
    public static void main(String[] args) {
        int number = 567;
        if (number % 100 >= 11 && number % 100 <= 19) {
            System.out.println(number + " котов");
        } else {
            if (number % 10 == 1) {
                System.out.println(number + " кот");
            } else if (number % 10 >= 2 && number % 10 <= 4) {
                System.out.println(number + " кот");
            } else if (number % 10 == 0 || (number % 10 >= 5 && number % 10 <= 9)) {
                System.out.println(number + " котов");
            }
        }
    }
}
