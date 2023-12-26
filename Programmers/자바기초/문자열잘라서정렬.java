import java.util.*;

class Solution {
    public String[] solution(String myString) {
        ArrayList<String> list = new ArrayList<>();
        String[] tmp = myString.split("x");
        for (String ele : tmp) {
            if (!ele.isEmpty()) {
                list.add(ele);
            }    
        }
        
        Collections.sort(list);
        
        
        String[] answer = new String[list.size()];
        for (int i = 0 ; i < list.size() ; i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}