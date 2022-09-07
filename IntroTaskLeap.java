public class IntroTaskLeap {
    public static void main(String[] args) {
        int year = 2022;
        if (year%4!=0) {
            System.out.println("Год не високосный");
        } else if (year%100==0 && year%400!=0) {
            System.out.println("Год не високосный");
        } else {
            System.out.println("Год високосный");
        }
    }
}
