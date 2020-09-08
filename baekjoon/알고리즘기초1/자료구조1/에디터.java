package baekjoon.알고리즘기초1.자료구조1;

import com.sun.scenario.effect.impl.sw.sse.SSEBlend_SRC_OUTPeer;

import java.util.Scanner;
import java.util.Stack;

public class 에디터 {
    public static void main(String[] args) {

        Stack<Character> stack0 = new Stack<>();
        Stack<Character> stack1 = new Stack<>();
        Scanner sc = new Scanner(System.in);
        String msg = sc.nextLine();
        for(int i = 0; i < msg.length(); i++) {
            stack0.push(msg.charAt(i));
        }
        int count = sc.nextInt();
        sc.nextLine();

        for(int i = 0; i < count; i++) {
            String command = sc.nextLine();
            String[] com = command.split(" ");
            if(com[0].equals("L")) {
                if(stack0.isEmpty()) {
                    continue;
                }
                stack1.push(stack0.pop());

            } else if(com[0].equals("D")) {
                if(stack1.isEmpty()) {
                    continue;
                }
                stack0.push(stack1.pop());

            } else if(com[0].equals("B")) {
                if(stack0.isEmpty()) {
                    continue;
                }
                stack0.pop();
            } else if(com[0].equals("P")) {
                stack0.push(com[1].charAt(0));
            }
        }
        System.out.println(stack0.size());
        StringBuilder answer = new StringBuilder();
        for(int i = 0; i < stack0.size(); i++) {
            answer.append(stack0.pop());
        }
        System.out.println(stack1.size());
        System.out.println(stack1.toString());
        for(int i = 0; i < stack1.size(); i++) {
            answer.append(stack1.pop());
        }
        answer.reverse();
        System.out.println(answer);

    }
}
