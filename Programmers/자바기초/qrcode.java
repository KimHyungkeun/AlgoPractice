class Solution {
    public String solution(int q, int r, String code) {
        String answer = "";
        int[] idxModule = new int[code.length()];
        
        for (int i = 0 ; i < code.length() ; i++) {
            if (i % q == r) {
                answer += Character.toString(code.charAt(i));
            }
        }
        
        return answer;
    }
}