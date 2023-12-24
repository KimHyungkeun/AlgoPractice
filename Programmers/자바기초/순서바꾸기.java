class Solution {
    public int[] solution(int[] num_list, int n) {
        int[] answer = new int[num_list.length];
        int idx = n;
        
        for (idx = n ; idx < num_list.length ; idx++) {
            answer[idx-n] = num_list[idx];
        }
        
        for (int j = 0 ; j < n ; j++) {
            answer[idx-n+j] = num_list[j];
        }
        
        
        return answer;
    }
}