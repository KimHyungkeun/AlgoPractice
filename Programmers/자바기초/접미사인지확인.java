class Solution {
    public int solution(String my_string, String is_suffix) {
        int answer = 0;
        if (my_string.length() - is_suffix.length() < 0) {
            return answer;
        }
        
        int start_idx = my_string.length() - is_suffix.length();
        
        if (my_string.substring(start_idx).equals(is_suffix)) {
            answer = 1;
        }
        return answer;
    }
}