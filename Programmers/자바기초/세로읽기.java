class Solution {
    public String solution(String my_string, int m, int c) {
        String answer = "";
        int row = my_string.length() / m;
        String[][] strArr = new String[row][m];
        
        int colNum = 0;
        int j = 0;
        for (int i = 0 ; i < my_string.length() ; i++) {
            strArr[colNum][j%m] = Character.toString(my_string.charAt(i));
            j++;
            if (j%m == 0) {
                colNum++;
            }
        }
        
        for (int k = 0 ; k < row ; k++) {
                answer += strArr[k][c-1];
        }
        
        
        return answer;
    }
}