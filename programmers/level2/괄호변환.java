import java.util.*;

class Solution {
    int position;

    public String solution(String p) {
        if (p.isEmpty()) { return p; }
        boolean check = check(p);
        String u = p.substring(0, position);
        String v = p.substring(position, p.length());

        if(check) {
            return u + solution(v);
        }

        String str = "(" + solution(v) + ")";

        for(int i = 1; i < u.length() - 1; i++) {
            if(u.charAt(i) == '(') {
                str += ")";
            } else {
                str += "(";
            }
        }
        return str;
    }

    boolean check(String ex) {

        boolean check = true;
        int countLeft = 0;
        int countRight = 0;
        Stack<Character> stack = new Stack<Character>();

        for (int i = 0; i < ex.length(); i++) {
            if (ex.charAt(i) == '(') {
                countLeft++;
                stack.push(ex.charAt(i));
            } else {
                countRight++;
                if (stack.isEmpty()) {
                    check = false;
                } else {
                    stack.pop();
                }
            }

            if(countLeft == countRight) {
                position = i + 1;
                return check;
            }
        }
        return check;
    }
}