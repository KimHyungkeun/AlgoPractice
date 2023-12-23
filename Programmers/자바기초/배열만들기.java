import java.util.*;

class Solution {
    public int[] solution(int n, int k) {
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = k ; i <= n ; i+=k) {
            if (i % k == 0) {
                list.add(i);
            }
        }
        
        int[] answer = new int[list.size()];
        int idx = 0;
        for (Integer ele : list) {
            answer[idx] = ele;
            idx ++;
        }
        return answer;
    }
}