public class IntroTaskSameDigits {
    public static void main(String[] args) {
        int x = 366;
        if (x<=10) {
            System.out.println("Однозначное число, условие не может быть выполнено");
        }
        if (x%10 == (x/10)%10) {
            System.out.println("На конце числа две одинаковые цифры");
        } else {
            System.out.println("На конце числа две разные цифры");
        }
    }
}
