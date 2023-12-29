class Solution {
    public static int[][] solution(int n) {
        int[][] answer = new int[n][n];
        int num = 0;
        int i=0;
        int j=0;
        String direction = "right";

        while (num < n*n) {
            
            num++;
            if (direction.equals("right")) {                
                answer[i][j] = num;
                j++;
                if (j == n || answer[i][j] != 0) {
                    j--;
                    i++;
                    direction = "down";
                    continue;
                }
                
            }
            
            else if (direction.equals("down")) {        
                answer[i][j] = num;
                i++;
                if (i == n || answer[i][j] != 0) {
                    i--;
                    j--;
                    direction = "left";
                    continue;
                }
            }
            
            else if (direction.equals("left")) {
                answer[i][j] = num;
                j--;
                if (j < 0 || answer[i][j] != 0) {
                    j++;
                    i--;
                    direction = "up";
                    continue;
                }
            }
            
            else if (direction.equals("up")) {
                answer[i][j] = num;
                i--;
                if (i < 0 || answer[i][j] != 0) {
                    i++;
                    j++;
                    direction = "right";
                    continue;
                }
                
            }

            else;
            
        }

        return answer;
    }
}