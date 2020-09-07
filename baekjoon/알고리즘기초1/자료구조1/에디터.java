package baekjoon.알고리즘기초1.자료구조1;

import java.util.Scanner;
import java.util.Stack;

public class 에디터 {
    public static void main(String[] args) {

        Stack<Character> stack = new Stack<>();
        Scanner sc = new Scanner(System.in);
        String msg = sc.nextLine();
        for(int i = 0; i < msg.length(); i++) {
            stack.push(msg.charAt(i));
        }
        int count = sc.nextInt();
        sc.nextLine();

        for(int i = 0; i < count; i++) {
            String command = sc.nextLine();
            System.out.println(command);
        }

    }
}
