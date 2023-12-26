import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        Stack<Integer> stack = new Stack<>();
        int i = 0;
        while(i != arr.length) {
            if (stack.size() == 0) {
                stack.push(arr[i]);
                i++;
            } else if (stack.size() != 0 && stack.get(stack.size()-1) == arr[i]) {
                stack.pop();
                i++;
            } else {
                stack.push(arr[i]);
                i++;
            }
        }
        
        int[] answer;
        if (stack.size() == 0) {
            answer = new int[1];
            answer[0] = -1;
        } else {
            answer = new int[stack.size()];
            for (int k = 0 ; k < stack.size() ; k++) {
                answer[k] = stack.get(k);
            }
        }
        
        return answer;
    }
}