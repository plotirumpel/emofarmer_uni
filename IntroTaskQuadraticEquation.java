public class IntroTaskQuadraticEquation  {
    public static void main(String[] args) {
        int a = 5;
        int b = 78;
        int c = 1;
        if (a==0) {
            if (b==0) {
                if (c==0) {
                    System.out.println("Решений бесконечно много");
                } else {
                    System.out.println("Решений нет");
                }
            } else {
                System.out.println("Одно решение: x = " + -c/b);
            }
        } else {
            double d = Math.pow(b,2) - 4*a*c;
            if (d>0) {
                System.out.println("Два решения: x1 = " + (-b-Math.pow(d,0.5))/(2*a) + "x2 = "+ (-b+Math.pow(d,0.5))/(2*a));
            } else if (d<0) {
                System.out.println("Решений нет");
            } else {
                System.out.println("Одно решение: x = " + -b/(2*a));
            }
        }
    }
}
