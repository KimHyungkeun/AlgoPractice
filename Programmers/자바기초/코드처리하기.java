class Solution {
    public String solution(String code) {
        String answer = "";
        String mode = "0";

        for (int idx = 0 ; idx < code.length() ; idx++) {
             if (mode.equals("0")) {
                if (code.charAt(idx) != '1' && idx % 2 == 0) {
                    answer += Character.toString(code.charAt(idx));
                } 
                 
                if (code.charAt(idx) == '1'){
                    mode = "1";
                }
              }
             
             else {
                if (code.charAt(idx) != '1' && idx % 2 != 0) {
                    answer += Character.toString(code.charAt(idx));
                } 
                 
                if (code.charAt(idx) == '1') {
                    mode = "0";
                }
             }
                  
        }
        
        if (answer.length() == 0) {
            answer = "EMPTY";
        }
        
        return answer;
    }
}