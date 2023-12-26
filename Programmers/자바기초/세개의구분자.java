import java.util.*;
class Solution {
    public String[] solution(String myStr) {
        ArrayList<String> list = new ArrayList<>();
        String tmp = "";
        for (int i = 0 ; i < myStr.length() ; i++) {
            String val = Character.toString(myStr.charAt(i));
            if(val.equals("a") || val.equals("b") || val.equals("c")) {
                if (tmp.length() > 0) {
                    list.add(tmp);
                }               
                tmp = "";
            } else {
                tmp += val;
            }
        }
        if (tmp.length() > 0) {
            list.add(tmp);
        }      
        
        String[] answer;
        if (list.size() == 0) {
            answer = new String[1];
            answer[0] = "EMPTY";
        }
        
        else {
            answer = new String[list.size()];
            for (int i = 0 ; i < list.size() ; i++) {
                answer[i] = list.get(i);
            }
        }
        
        return answer;
    }
}