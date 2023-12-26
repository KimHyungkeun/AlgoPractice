import java.util.*;
class Solution {
    public int[] solution(int[] arr, int k) {
        Stack<Integer> stack = new Stack<Integer>();
        for (int ele : arr) {
            if(!stack.contains(ele)) {
                stack.push(ele);
            }
        }
        
        Integer[] resultArr = stack.toArray(new Integer[0]);
            
        int[] answer = new int[k];
        for (int i = 0 ; i < k ; i++) {
            if (i < resultArr.length) {
                answer[i] = resultArr[i];
            } else {
                answer[i] = -1;
            }
            
        }
        
        
        return answer;
    }
}