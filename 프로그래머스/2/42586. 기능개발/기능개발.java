import java.util.ArrayList;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        
        ArrayList<Integer> result = new ArrayList<>();
        
        int n = progresses.length;
        int workday = 0;
        
        for (int i = 0; i < n; i++) {
            int remain = 100 - progresses[i] - speeds[i] * workday;
            workday += (remain % speeds[i] == 0) ? remain / speeds[i] : remain / speeds[i] + 1;
 
            int count = 0;
            
            while (i < n && progresses[i] + speeds[i] * workday >= 100) {
                System.out.println(progresses[i] + speeds[i] * workday);
                System.out.println(workday);
                
                count++;
                i++;
            }
            i--;
            
            result.add(count);
        }
        
        int[] answer = new int[result.size()];
        
        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }
        
        return answer;
    }
}