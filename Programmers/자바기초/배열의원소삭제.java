import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        Set<Integer> set = new HashSet<>();
        for (int ele : delete_list) {
            set.add(ele);
        }
        ArrayList<Integer> list = new ArrayList<>();
        
        for (int i = 0 ; i < arr.length ; i++) {
            if (!set.contains(arr[i])) {
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