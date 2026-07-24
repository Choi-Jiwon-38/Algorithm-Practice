import java.util.HashMap;

class Solution {
    public int solution(String[][] clothes) {
        HashMap<String, Integer> map = new HashMap<>();
        
        for (String[] cloth: clothes) {
            String key = cloth[1];
            map.put(key, map.getOrDefault(key, 0) + 1);
        }
        
        
        int answer = 1;
        
        for (int x: map.values()) {
            answer *= x + 1;
        }
        
    
        return answer - 1;
    }
}