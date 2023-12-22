class Solution {
    public int solution(String my_string, String is_prefix) {
        int answer = 0;
        int end_idx = is_prefix.length();
        
        if (my_string.length() < is_prefix.length()) {
            return answer;
        }
        
        if (my_string.substring(0,end_idx).equals(is_prefix)) {
            answer = 1;
        }
        
        return answer;
    }
}