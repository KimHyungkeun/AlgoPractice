import java.util.*;
class Solution {
    public String solution(String myString) {
        String answer = "";
        String[] strArr = myString.split("");
        
        for (int i = 0 ; i < strArr.length ; i++) {
            if (strArr[i].charAt(0) <= "l".charAt(0)) {
                strArr[i] = "l";
            }
        }
        
        answer = String.join("",strArr);
        return answer;
    }
}