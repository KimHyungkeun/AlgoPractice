class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = {};
        for (int[] q : queries) {
            for (int i = q[0] ; i <= q[1] ; i++) {
                if (i == 0 || i % q[2] == 0) {
                    arr[i] ++;
                }
            }

        }
        
        return arr;
    }
}