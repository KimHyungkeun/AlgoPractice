import java.util.*;

class Solution {
    public int solution(int a, int d, boolean[] included) {
        int answer = 0;
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 0 ; i < included.length ; i ++) {        
            if (included[i]) {
                list.add(a);
            }
            a += d;
        }
        
        for (Integer ele : list) {
            answer += ele;
        }
        
        return answer;
    }
}