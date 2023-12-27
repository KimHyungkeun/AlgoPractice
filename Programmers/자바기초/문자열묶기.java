import java.util.*;

class Solution {
    public int solution(String[] strArr) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (String str : strArr) {
            int key = str.length();
            if (map.containsKey(key)) {
                int val = map.get(key);
                val++;
                map.replace(key, val);
            } else {
                map.put(key, 1);
            }
        }
        
        int answer = 0;
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (answer < entry.getValue()) {
                answer = entry.getValue();
            }
        }

        
        
        return answer;
    }
}