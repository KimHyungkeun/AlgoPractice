class Solution {
    public String solution(String my_string, String alp) {
        String[] strArr = new String[my_string.length()];
        String answer = "";
        for (int i = 0 ; i < my_string.length() ; i++) {
            String ele = Character.toString(my_string.charAt(i));
            if (ele.equals(alp)) {
                strArr[i] = alp.toUpperCase();
            } else {
                strArr[i] = ele;
            }
        }
        
        answer = String.join("",strArr);
        return answer;
    }
}