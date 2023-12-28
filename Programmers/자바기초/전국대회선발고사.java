import java.util.*;

class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0 ; i < rank.length ; i++) {
            if (attendance[i]) {
                map.put(rank[i], i);
            }
        }
        
        ArrayList<Integer> keySet = new ArrayList<>(map.keySet());
        Collections.sort(keySet);
        
        int answer = 0;
        int idx = 0;
        for (Integer key : keySet) {
            if (idx == 0) {
                answer += (map.get(key) * 10000);
            } else if (idx == 1) {
                answer += (map.get(key) * 100);
            } else if (idx == 2) {
                answer += map.get(key);
            } else {
                break;
            }
            
            idx++;
        }
        
        
        
        return answer;
    }
}