class Solution {
    public String solution(String my_string, int s, int e) {
        String answer = "";
        String[] strArr = new String[my_string.length()];
        for (int i = 0 ; i < my_string.length(); i++) {
            strArr[i] = Character.toString(my_string.charAt(i));
        }
        
        int mid = (s+e) / 2;
        String tmp = "";
        for (int j = s; j <= mid ; j++) {
            tmp = strArr[j];
            strArr[j] = strArr[e];
            strArr[e] = tmp;
            e--;
        }
        
        answer = String.join("", strArr);
        return answer;
    }
}