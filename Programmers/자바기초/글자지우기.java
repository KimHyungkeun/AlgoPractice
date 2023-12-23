class Solution {
    public String solution(String my_string, int[] indices) {
        String answer = "";
        String[] strArr = new String[my_string.length()];
        for (int i = 0 ; i < my_string.length() ; i++) {
            strArr[i] = Character.toString(my_string.charAt(i));
        }
        
        for (int idx : indices) {
            strArr[idx] = "";
        }
        
        answer = String.join("",strArr);
        
        return answer;
    }
}