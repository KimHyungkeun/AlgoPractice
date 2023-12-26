import java.util.*;

class Solution {
    public String solution(String rny_string) {
        ArrayList<String> list = new ArrayList<>();
        for (int i = 0 ; i < rny_string.length() ; i++) {
            if (rny_string.charAt(i) == 'm') {
                list.add("r");
                list.add("n");
            } else {
                list.add(Character.toString(rny_string.charAt(i)));
            }
        }
        
        String[] result = list.toArray(new String[list.size()]);
        String answer = String.join("", result);
        return answer;
    }
}