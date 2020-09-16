package baekjoon.알고리즘기초1.자료구조1;

import java.util.*;

public class 큐 {
    public static void main(String[] args) {
        int num = 0;
        Queue<Integer> queue = new LinkedList<>();
        Scanner sc = new Scanner(System.in);

        int count = sc.nextInt();

        for(int i = 0; i < count; i++) {
            String msg0 = sc.next();
            if(msg0.equals("push")) {
                num = sc.nextInt();
                queue.add(num);
            } else if(msg0.equals("pop")) {
                System.out.println(queue.isEmpty()?-1:queue.poll());
            } else if(msg0.equals("front")) {
                System.out.println(queue.isEmpty()?-1:queue.peek());
            } else if(msg0.equals("back")) {
                System.out.println(queue.isEmpty()?-1:num);
            } else if(msg0.equals("size")) {
                System.out.println(queue.size());
            } else if(msg0.equals("empty")) {
                System.out.println(queue.isEmpty()?1:0);
            }
        }

    }
}
