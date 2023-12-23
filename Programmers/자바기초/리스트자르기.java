import java.util.*;

class Solution {
    public int[] solution(int n, int[] slicer, int[] num_list) {      
        ArrayList<Integer> numArr = new ArrayList<>();
        List<Integer> listArr = new ArrayList<>();
        
        for (int num : num_list) {
            numArr.add(num);
        }
        
        if (n == 1) {
            listArr = numArr.subList(0, slicer[1]+1);
        } else if (n == 2) {
            listArr = numArr.subList(slicer[0], numArr.size());
        } else if (n == 3) {
            listArr = numArr.subList(slicer[0], slicer[1]+1);
        } else {
            ArrayList<Integer> tmp = new ArrayList<>();
            for (int i = slicer[0] ; i <= slicer[1] ; i += slicer[2]) {
                tmp.add(num_list[i]);
            }
            listArr = tmp;
        }
        
        int[] answer = new int[listArr.size()];
        for (int i = 0 ; i < answer.length ; i++) {
            answer[i] = listArr.get(i);
        }
        return answer;
    }
}