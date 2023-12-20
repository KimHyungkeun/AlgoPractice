import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        ArrayList<Integer> list = new ArrayList<>();
        int last_ele = 0;
        
        if (num_list[num_list.length-2] < num_list[num_list.length-1]) {
            last_ele = num_list[num_list.length-1] - num_list[num_list.length-2];
        } else {
            last_ele = num_list[num_list.length-1] * 2;
        }
        
        for (int ele : num_list) {
            list.add(ele);
        }
        list.add(last_ele);   
        
        int[] answer = new int[num_list.length+1];
        int idx = 0;
        for (Integer ele : list) {
            answer[idx] = ele;
            idx ++;
        }

        return answer;
    }
}