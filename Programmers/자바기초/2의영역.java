import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        
        ArrayList<Integer> idxList = new ArrayList<>();
        for (int i = 0 ; i < arr.length ; i++) {
            if (arr[i] == 2) {
                idxList.add(i);
            }
        }
        
        if (idxList.size() == 0) {
            int[] answer = {-1};
            return answer;
        }
        
        int startIdx = idxList.get(0);
        int endIdx = idxList.get(idxList.size()-1);
        
        int[] answer = new int[endIdx-startIdx+1];
        
        int idx = 0;
        for (int i = startIdx ; i <= endIdx ; i++) {
            answer[idx] = arr[i];
            idx++;
        }
        
        return answer;
    }
}