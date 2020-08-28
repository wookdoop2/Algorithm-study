package baekjoon.알고리즘기초1.알고리즘시작;

import java.util.Scanner;

public class AplusB_7 {
    public static void main(String[] args) {
        int count, num0, num1;
        Scanner sc = new Scanner(System.in);

        count = sc.nextInt();
        for(int i = 1; i < count + 1; i++) {
            num0 = sc.nextInt();
            num1 = sc.nextInt();
            System.out.println("Case #" + i + ": " + (num0 + num1));
        }
    }
}