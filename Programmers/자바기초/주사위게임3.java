import java.util.*;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;
        if (a == b && b == c && c == d) {
            answer = a * 1111;
            return answer;
        } else {
            int[] arr = {a,b,c,d};
            
            Map<Integer, Integer> map = new HashMap<>();
            for (int ele : arr) {
                if(map.containsKey(ele)) {
                    int val = map.get(ele) + 1;
                    map.put(ele, val);
                } else {
                    map.put(ele, 1);
                }
            }
            
            List<Map.Entry<Integer, Integer>> entryList = new LinkedList<>(map.entrySet());
            entryList.sort(Map.Entry.comparingByValue());
            
            if (entryList.size() == 4) {
                for(Map.Entry<Integer, Integer> entry : entryList){
                    answer = entry.getKey();
                    break;
                }
            } else if (entryList.size() == 3) {
                int idx = 0;
                int tmp = 1;
                for(Map.Entry<Integer, Integer> entry : entryList){
                    tmp *= entry.getKey();
                    idx ++;
                    if (idx == 2) {
                        answer = tmp;
                        break;
                    }
                }
            } else {
                int[] key = {0,0};
                int[] val = {0,0};
                int idx = 0;
                for(Map.Entry<Integer, Integer> entry : entryList){
                    key[idx] = entry.getKey();
                    val[idx] = entry.getValue();
                    idx++;
                }
                
                if (val[0] == val[1]) {
                    answer = (key[0] + key[1]) * Math.abs(key[0]-key[1]);
                } else if (val[0] > val[1]) {
                    answer = (int)Math.pow((10 * key[0] + key[1]),2);
                } else {
                    answer = (int)Math.pow((10 * key[1] + key[0]),2);
                }
                
            }          
            
        }
        
        return answer;
    }
}