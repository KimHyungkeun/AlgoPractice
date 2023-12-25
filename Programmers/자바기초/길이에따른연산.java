class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int result;
        if (num_list.length >= 11) {
            result = 0;
            for (int num : num_list) {
                result += num;
            }
            
        } else {
            result = 1;
            for (int num : num_list) {
                result *= num;
            }
        }
        answer = result;
        return answer;
    }
}