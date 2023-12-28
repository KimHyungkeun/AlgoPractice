class Solution {
    public String solution(String n_str) {
        String answer = "";
        int i;
        for (i = 0 ; i < n_str.length() ; i++) {
            if (n_str.charAt(i) != '0') {
                break;
            }
        }
        
        answer = n_str.substring(i);
        return answer;
    }
}