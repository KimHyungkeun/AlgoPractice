import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[][] intervals) {
        ArrayList<Integer> list = new ArrayList<>();
        
        for (int[] q : intervals) {
            for (int i = q[0] ; i <= q[1] ; i++) {
                list.add(arr[i]);
            }
        }
        
        int[] answer = new int[list.size()];
        for (int i = 0 ; i < list.size() ; i++) {
            answer[i] = list.get(i);
        }
        
        
        return answer;
    }
}