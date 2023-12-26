import java.util.*;

class Solution {
    public int[] solution(String myString) {
        ArrayList<Integer> idxList = new ArrayList<>();
        
        for (int i = 0 ; i < myString.length() ; i++) {
            if (myString.charAt(i) == 'x') {
                idxList.add(i);
            }
        }
          
        ArrayList<Integer> gapList = new ArrayList<>();
        for (int i = 0 ; i < idxList.size() ; i++) {
            if (i == 0) {
                gapList.add(idxList.get(i));
                gapList.add(idxList.get(i+1) - idxList.get(i) - 1);
            } else if (i == idxList.size() - 1) {
                gapList.add(myString.length() - idxList.get(i) - 1);
            } else {
                gapList.add(idxList.get(i+1) - idxList.get(i) - 1);
            }
                     
        }
        
        int[] answer = gapList.stream().mapToInt(i -> i).toArray();
        return answer;
    }
}