package programmers.level2;

import java.util.*;

public class 수식최대화 {

    public static void main(String[] args) {
        String expression = "100-200*300-500+20";

        char[] operations;

        List<Character> operation = new ArrayList<>();
        if (expression.contains("+")) {
            operation.add('+');
        }
        if (expression.contains("-")) {
            operation.add('-');
        }
        if (expression.contains("*")) {
            operation.add('*');
        }
        System.out.println(operation);

        operations = new char[operation.size()];
        for (int i = 0; i < operations.length; i++) {
            operations[i] = operation.get(i);
            System.out.println(operations[i]);
        }

    }
}
