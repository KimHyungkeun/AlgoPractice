class Solution {
    public int solution(int[] arr) {
        int answer = 0;
        
        while (true) {
            int[] before = new int[arr.length];
            for (int i = 0 ; i < arr.length ; i++) {
                before[i] = arr[i];
            }
            
            for (int i = 0 ; i < arr.length ; i++) {
                if (arr[i] >= 50 && arr[i] % 2 == 0) {
                    arr[i] = arr[i] / 2;
                }
                else if (arr[i] < 50 && arr[i] % 2 != 0) {
                    arr[i] = arr[i] * 2 + 1;
                } 
                else ;    
            }
            
            boolean isTrue = true;
            for (int i = 0 ; i < arr.length ; i++) {
                if (arr[i] != before[i]) {
                    isTrue = false;
                    break;
                }
            }
            
            if (isTrue) {
                break;
            }
            
            answer += 1;
        }     
        
        return answer;
    }
    
}