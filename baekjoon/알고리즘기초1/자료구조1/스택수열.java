package baekjoon.알고리즘기초1.자료구조1;

import java.util.Scanner;
import java.util.Stack;

public class 스택수열 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Stack<Character> stack = new Stack<>();
        int num0 = 0;
        int count = sc.nextInt();

        for(int i = 0; i < count; i++) {
            int num1 = sc.nextInt();
            while (num0 < num1) {
                stack.push('+');
                num0++;
            }
            stack.push('-');
        }

        Character[] answer = new Character[stack.size()];
        for(int i = 0; i < answer.length; i++) {
            answer[i] = stack.pop();
        }
        for(int i = answer.length - 1; i >= 0; i--) {
            System.out.println(answer[i]);
        }
    }
}