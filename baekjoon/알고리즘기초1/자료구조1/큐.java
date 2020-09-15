package baekjoon.알고리즘기초1.자료구조1;

import java.util.*;

public class 큐 {
    public static void main(String[] args) {
        int count, num = 0;
        String msg0, msg1;
        Queue<Integer> queue = new LinkedList<>();
        Scanner sc = new Scanner(System.in);

        count = sc.nextInt();

        for(int i = 0; i < count; i++) {
            msg0 = sc.next();
            if(msg0.contains("push")) {
                msg1 = msg0.split(" ")[1];
                num = Integer.parseInt(msg1);
                queue.add(num);
            } else if(msg0.contains("front")) {
                System.out.println(queue.isEmpty()?-1:queue.peek());
            } else if(msg0.contains("back")) {
                System.out.println(queue.isEmpty()?-1:num);
            } else if(msg0.contains("size")) {
                System.out.println(queue.isEmpty()?-1:queue.size());
            } else if(msg0.contains("empty")) {
                System.out.println(queue.isEmpty()?-1:0);
            }
        }

    }
}
