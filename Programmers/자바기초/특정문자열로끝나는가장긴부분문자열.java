class Solution {
    public String solution(String myString, String pat) {
        String answer = "";
        int patLength = pat.length();
        
        for (int i = myString.length() - patLength ; i >= 0 ; i--) {
            String subStr = myString.substring(i, i + patLength);
            if (subStr.equals(pat)) {
                answer = myString.substring(0, i+patLength);
                break;
            }
        }
        return answer;
    }
}