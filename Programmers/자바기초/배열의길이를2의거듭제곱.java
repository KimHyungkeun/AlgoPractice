class Solution {
    public int[] solution(int[] arr) {    
        int arrLength = arr.length;
        
        int n = 0;
        int gap;
        while (Math.pow(2, n) < arr.length) {
            n++;
        }
        gap = (int)Math.pow(2, n) - arr.length;
        
        int[] answer = new int[arr.length + gap];
        for (int i = 0 ; i < answer.length ; i++) {
            if (i < arr.length) {
                answer[i] = arr[i];
            } else {
                answer[i] = 0;
            }
        }
        
       
        return answer;
    }
}