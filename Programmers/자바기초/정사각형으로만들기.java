class Solution {
    public int[][] solution(int[][] arr) {
        int[][] answer = {};
        
        if (arr.length == arr[0].length) {
            answer = arr;
        } else if (arr.length < arr[0].length) {
            answer = new int[arr[0].length][arr[0].length];
            for (int i = 0 ; i < answer.length ; i++) {
                for (int j = 0 ; j < answer.length; j++) {
                    if (i < arr.length) {
                        answer[i][j] = arr[i][j];
                    } else {
                        answer[i][j] = 0;
                    }
                }
            }
        } else {
            answer = new int[arr.length][arr.length];
            for (int i = 0 ; i < answer.length ; i++) {
                for (int j = 0 ; j < answer.length; j++) {
                    if (j < arr[0].length) {
                        answer[i][j] = arr[i][j];
                    } else {
                        answer[i][j] = 0;
                    }
                }
            }
        }
        
        return answer;
    }
}