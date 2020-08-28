package baekjoon.알고리즘기초1.알고리즘시작;

import java.util.Scanner;

public class AplusB_3 {
    public static void main(String[] args) {

        int count, num0, num1;
        Scanner sc = new Scanner(System.in);

        count = sc.nextInt();

        for (int i = 0; i < count; i++) {
            num0 = sc.nextInt();
            num1 = sc.nextInt();
            System.out.println(num0 + num1);
        }
    }
}
