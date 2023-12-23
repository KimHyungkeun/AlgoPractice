import java.util.*;

class Solution {
    public int[] solution(String my_string) {
        Map<String, Integer> hash = new HashMap<String, Integer>();
        for (int i = 65 ; i <= 90 ; i++) {
            hash.put(Character.toString((char)i),0);
        }
        
        for (int i = 97 ; i <= 122 ; i++) {
            hash.put(Character.toString((char)i),0);
        }

        for (int i = 0 ; i < my_string.length() ; i++) {
            String key = Character.toString(my_string.charAt(i));
            int val = hash.get(key);
            val++;
            hash.replace(key, val);
        }
        
        int idx = 0;
        int[] answer = new int[hash.size()];
        for (String key : hash.keySet()) {
            answer[idx] = hash.get(key);
            idx++;
        }

        return answer;
    }
}