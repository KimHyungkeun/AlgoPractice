import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        Stack<Integer> stack = new Stack<>();
        int i = 0;
        while (i < arr.length) {
            if (stack.size() == 0) {
                stack.push(arr[i]);
                i++;
            } else if (stack.size() != 0) {
                if (stack.get(stack.size()-1) >= arr[i]) {
                    stack.pop();
                } else {
                    stack.push(arr[i]);
                    i++;
                }
            }
            
        }
        
        int[] stk = new int[stack.size()];
        for (int idx = 0 ; idx < stack.size() ;idx++) {
            stk[idx] = stack.get(idx);
        }
        return stk;
    }
}