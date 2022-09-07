public class IntroTasks {

    public static void main(String[] args){

        int x = 1567;
        if (x>=100 && x<1000) {
            System.out.println("В числе ровно три цифры");
        } else {
            System.out.println("Число не трёхзначное");
        }


        x = 555;
        if (x%10==5) {
            System.out.println("Число оканчивается на 5");
        } else {
            System.out.println("Число не оканчивается на 5");
        }


        x = 366;
        if (x<=10) {
            System.out.println("Однозначное число, условие не может быть выполнено");
        }
        if (x%10 == (x/10)%10) {
            System.out.println("На конце числа две одинаковые цифры");
        } else {
            System.out.println("На конце числа две разные цифры");
        }

        int year = 2022;
        if (year%4!=0) {
            System.out.println("Год не високосный");
        } else if (year%100==0 && year%400!=0) {
            System.out.println("Год не високосный");
        } else {
            System.out.println("Год високосный");
        }

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

        x = 567;
        int i;
        int check = 0;
        double squareRoot = Math.pow(x,0.5);
        for(i=2;i<=squareRoot + 1;i++)
            {
                if (x%i==0) {
                    System.out.println("Число не простое");
                    check = 1;
                    break;
            }
        }
        if (check==0) {
            System.out.println("Число простое");
        }
    }
}
