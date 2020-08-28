package baekjoon.알고리즘기초1.알고리즘시작;

import java.util.Scanner;

public class AplusB_6 {
    public static void main(String[] args) {

        int count;
        String[] num;
        Scanner sc = new Scanner(System.in);

        count = sc.nextInt();

        for(int i = 0; i < count; i++) {
            num = sc.next().split(",");
            System.out.println(Integer.parseInt(num[0]) + Integer.parseInt(num[1]));
        }
    }
}
