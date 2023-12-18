import java.util.*;

class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        
        String[] strArr = my_string.split(""); 
        ArrayList<String> list = new ArrayList<String>(Arrays.asList(strArr));
        
        for (int i = s ; i < s + overwrite_string.length() ; i++) {
            list.set(i, Character.toString(overwrite_string.charAt(i-s)));
            System.out.print(list.get(i));
        }
        
        for (int i = 0 ; i < list.size() ; i ++) {
            answer += list.get(i);
        }
        return answer;
    }
}