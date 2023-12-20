class Solution {
    public String solution(int[] numLog) {
        String answer = "";
        
        for (int i = 1 ; i < numLog.length ; i++) {
            if (numLog[i-1] + 1 == numLog[i]) {
                answer += Character.toString('w');
            }
            
            if (numLog[i-1] - 1 == numLog[i]) {
                answer += Character.toString('s');
            }
            
            if (numLog[i-1] + 10 == numLog[i]) {
                answer += Character.toString('d');
            }
            
            if (numLog[i-1] - 10 == numLog[i]) {
                answer += Character.toString('a');
            }
        }
        
        return answer;
    }
}