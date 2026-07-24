import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> players = new HashMap<>();
        
        for (String p: participant) {
            if (players.containsKey(p)) {
                players.put(p, players.get(p) + 1);
            } else {
                players.put(p, 1);
            }
        }
        
        for (String c: completion) {
            players.put(c, players.get(c) - 1);
            if (players.get(c) == 0) {
                players.remove(c);
            }
        }
        
        System.out.println(players.keySet());
        
        
        String answer = "";
        for (String key: players.keySet()) {
            answer = key;
        }
        
        return answer;
    }
}