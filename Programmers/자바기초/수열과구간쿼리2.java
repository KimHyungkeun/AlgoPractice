import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[][] queries) {
     
        ArrayList<Integer> list = new ArrayList<>();
        
        for (int[] q : queries) {
            int[] tmp = Arrays.copyOfRange(arr, q[0], q[1]+1);
            int min = 1000001;
            int cnt = 0;
            for (int t : tmp) {
                if (t > q[2] && t < min) {
                    min = t;
                    cnt++;
                }
            }
            
            if (cnt == 0) {
                min = -1;
            }
            
            list.add(min);
        }
        
        int[] answer = new int[list.size()];
        for (int i = 0 ; i < list.size() ; i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}