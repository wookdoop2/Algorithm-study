package baekjoon.알고리즘기초1.자료구조1;

import java.util.*;

public class 괄호 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int count = sc.nextInt();
        sc.nextLine();

        for(int i = 0; i < count; i++) {
            boolean check = true;
            Stack<Character> stack = new Stack<>();
            String vps = sc.nextLine();
            for(int j = 0; j < vps.length(); j++) {
                if (vps.charAt(j) == ')') {
                    if(stack.isEmpty()) {
                        check = false;
                        break;
                    }
                    stack.pop();
                } else {
                    stack.push(vps.charAt(j));
                }
            }
            if(!stack.isEmpty()) {
                check = false;
            }

            if(check) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}

