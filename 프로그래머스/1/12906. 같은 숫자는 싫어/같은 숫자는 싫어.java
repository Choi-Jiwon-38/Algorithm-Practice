import java.util.*;

public class Solution {
    public ArrayList<Integer> solution(int []arr) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        for (int x: arr) {
            if (answer.size() > 0 && answer.get(answer.size() - 1) == x) {
                continue;
            } else {
                answer.add(x);
            }
        }
        
        
        
        return answer;
    }
}