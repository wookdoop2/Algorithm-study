package baekjoon.알고리즘기초1.자료구조1;

import java.util.*;

public class 단어뒤집기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int count = sc.nextInt();
        sc.nextLine();

        for(int i = 0; i < count; i++) {
            String msg = sc.nextLine();
            Stack<Character> stack = new Stack<>();
            for(int j = 0; j < msg.length(); j++) {
                if(msg.charAt(j) == ' ') {
                    while(!stack.isEmpty()) {
                        System.out.print(stack.pop());
                    }
                    System.out.print(" ");
                } else {
                    stack.push(msg.charAt(j));
                }
            }
            while(!stack.isEmpty()) {
                System.out.print(stack.pop());
            }
            System.out.println();
        }
    }
}
