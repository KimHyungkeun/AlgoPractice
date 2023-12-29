import java.util.*;
class Solution {
    public String[] solution(String[] picture, int k) {
        
        ArrayList<String> total = new ArrayList<>();

        int idx = 0;
        
        for (int i = 0 ; i < picture.length ; i++) {
            ArrayList<String> list = new ArrayList<>();
            for (int j = 0 ; j < picture[i].length() ; j++) {
                for(int t = 0 ; t < k ; t++) {
                    list.add(Character.toString(picture[i].charAt(j)));
                }
            }
            String[] result = list.stream().toArray(String[]::new);
            for (int p = 0 ; p < k ; p++) {
                total.add(String.join("",result));
            }
        }
        
        String[] totalResult = total.stream().toArray(String[]::new);
        String[] answer = totalResult;
        
        return answer;
    }
}