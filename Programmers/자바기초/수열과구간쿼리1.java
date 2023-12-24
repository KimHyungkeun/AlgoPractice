class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = {};
        for (int[] q : queries) {
            for (int i = q[0]; i <= q[1] ; i++) {
                arr[i]++;
            }
        }
        
        answer = arr;
        return answer;
    }
}