class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        String lowerString = myString.toLowerCase();
        String lowerPat = pat.toLowerCase();
        
        if (lowerString.contains(lowerPat)) {
            answer = 1;
        }
        return answer;
    }
}