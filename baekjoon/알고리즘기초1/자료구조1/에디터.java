package baekjoon.알고리즘기초1.자료구조1;

import java.io.*;
import java.util.*;

public class 에디터 {
    public static void main(String[] args) throws IOException {

        Stack<Character> stack0 = new Stack<>();
        Stack<Character> stack1 = new Stack<>();
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        String msg = sc.readLine();
        for(int i = 0; i < msg.length(); i++) {
            stack0.push(msg.charAt(i));
        }
        int count = Integer.parseInt(sc.readLine());

        for(int i = 0; i < count; i++) {
            String command = sc.readLine();
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
        StringBuilder answer = new StringBuilder();

        while(!stack0.isEmpty()) {
            answer.append(stack0.pop());
        }
        answer.reverse();

        while(!stack1.isEmpty()) {
            answer.append(stack1.pop());
        }
        System.out.println(answer);

    }
}
