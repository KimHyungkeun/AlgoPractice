class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int even_sum = 0;
        int odd_sum = 0;
        
        for (int i = 0 ; i < num_list.length ; i ++) {
            if (i % 2 == 0) {
                odd_sum += num_list[i];
            } else {
                even_sum += num_list[i];
            }
        }
        
        if (even_sum <= odd_sum) {
            answer = odd_sum;
        } else {
            answer = even_sum;
        }
        
        return answer;
    }
}