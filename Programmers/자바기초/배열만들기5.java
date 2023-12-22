import java.util.*;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        
        ArrayList<Integer> list = new ArrayList<>();
        
        for(String str : intStrs) {
            String subStr = str.substring(s,s+l);
            if (Integer.parseInt(subStr) > k) {
                list.add(Integer.parseInt(subStr));
            }
            
        }
        
        int[] answer = new int[list.size()];
        for (int i = 0 ; i < list.size() ;i++) {
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}