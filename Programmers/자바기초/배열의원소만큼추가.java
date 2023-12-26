import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        
        int size = Arrays.stream(arr).sum();
        int[] answer = new int[size];
        int idx = 0;
        
        for (int ele : arr) {
            for (int i = 0 ; i < ele ; i++) {
                answer[idx] = ele;
                idx++;
            }
        }
        
        
        return answer;
    }
}