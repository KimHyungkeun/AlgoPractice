class Solution {
    public String solution(String my_string, int[][] queries) {
        String answer = "";
        String[] stringArr = new String[my_string.length()];
        
        for (int i = 0 ; i < my_string.length() ; i++) {
            stringArr[i] = Character.toString(my_string.charAt(i));
        }
        
        for (int[] q : queries) {
            int mid = (q[0] + q[1]) / 2;
            String tmp = "";
            int lastIdx = q[1];
            for (int i = q[0] ; i <= mid ; i++) {
                tmp = stringArr[lastIdx];
                stringArr[lastIdx] = stringArr[i];
                stringArr[i] = tmp;
                lastIdx--;
            }
            
        }
        
        for (String ele : stringArr) {
            answer += ele;
        }
        return answer;
    }
}