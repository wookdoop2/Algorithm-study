package baekjoon.알고리즘기초1.자료구조1;

import java.util.*;

public class 스택 {
    public static void main(String[] args) {

        Stack<Integer> stack = new Stack<>();
        Scanner sc = new Scanner(System.in);
        int count = sc.nextInt();

        for(int i = 0; i < count; i++) {
            String msg = sc.next();
            if(msg.contains("push")) {
                int num = sc.nextInt();
                stack.push(num);
            }
            if(msg.contains("pop")) {
                System.out.println(stack.isEmpty()?-1:stack.pop());
            }
            if(msg.contains("top")) {
                System.out.println(stack.isEmpty()?-1:stack.peek());
            }
            if(msg.contains("size")) {
                System.out.println(stack.size());
            }
            if(msg.contains("empty")) {
                System.out.println(stack.isEmpty()?1:0);
            }
        }


    }
}
