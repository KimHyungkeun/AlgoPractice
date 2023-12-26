class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        int patLength = pat.length();
        
        for (int i = 0 ; i <= myString.length() - patLength ; i++) {
            String subStr = myString.substring(i, i + patLength);
            if (subStr.equals(pat)) {
                answer++;
            }
        }
        
        return answer;
    }
}