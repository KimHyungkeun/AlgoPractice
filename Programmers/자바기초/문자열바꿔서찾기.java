class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        String[] changeStr = new String[myString.length()];
        for (int i = 0 ; i < myString.length() ; i++) {
            if (myString.charAt(i) == 'A') {
                changeStr[i] = "B";
            } else {
                changeStr[i] = "A";
            }
        }
        
        String result = String.join("",changeStr);
        
        if (result.contains(pat)) {
            answer = 1;
        }
        
        return answer;
    }
}