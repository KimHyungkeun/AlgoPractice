import java.util.*;

class Solution {
    public String[] solution(String my_string) {
        ArrayList<String> list = new ArrayList<>();  
        String[] splitStr = my_string.split(" ");
        for (int i = 0 ; i < splitStr.length ; i++) {
            if (!splitStr[i].equals("")) {
                list.add(splitStr[i]);
            }
        }
        
        String[] answer = new String[list.size()];
        for (int i = 0 ; i < list.size() ; i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}