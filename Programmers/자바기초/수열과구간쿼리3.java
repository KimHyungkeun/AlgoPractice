class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = {};
        int tmp = 0;
        for (int[] query : queries) {
            tmp = arr[query[0]];
            arr[query[0]] = arr[query[1]];
            arr[query[1]] = tmp;
        }
        
        answer = arr;
        return answer;
    }
}