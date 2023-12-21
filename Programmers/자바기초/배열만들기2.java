public import java.util.*;

class Solution {
    public int[] solution(int l, int r) {  
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = l ; i <= r ; i++) {
            String strNum = Integer.toString(i);
            boolean isFlag = true;
            for (int j = 0 ; j < strNum.length() ; j++) {
                if (!Character.toString(strNum.charAt(j)).equals("0") && !Character.toString(strNum.charAt(j)).equals("5")) {
                    isFlag = false;
                    break;
                }
            }
            
            if (isFlag) {
                list.add(Integer.parseInt(strNum));
            }
            
        }
        
        if (list.size() == 0) {
            int[] answer = {-1};
            return answer;
        }
        
        int[] answer = new int[list.size()];
        for (int i = 0 ; i < list.size() ; i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
} 배열만들기2 {
    
}
