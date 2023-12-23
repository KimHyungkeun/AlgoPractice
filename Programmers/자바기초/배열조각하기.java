import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] query) {

        List<Integer> numArr = new ArrayList<>();
        
        for(int ele : arr) {
            numArr.add(ele);
        }
        
        for (int q = 0 ; q < query.length ; q++) {
            
            if (q % 2 == 0) {
                numArr = numArr.subList(0, query[q]+1);
            } else {
                numArr = numArr.subList(query[q], numArr.size());
            }
        }
        
        int[] answer = new int[numArr.size()];
        for (int i = 0 ; i < answer.length ; i++) {
            answer[i] = numArr.get(i);
        }
        
        return answer;
    }
}