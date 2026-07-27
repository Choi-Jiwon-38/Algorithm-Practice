import java.util.ArrayDeque;

class Solution {
    boolean solution(String s) {
        ArrayDeque<Character> stack = new ArrayDeque<>();
        
        for (char c: s.toCharArray()) {            
            if (stack.size() < 1) {
                stack.add(c);
            } else {
                if (stack.getLast() == '(' && c == ')') {
                    stack.removeLast();
                } else {
                    stack.add(c);
                }
            }
        }

        return stack.size() == 0 ? true : false;
    }
}