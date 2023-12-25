class Solution {
    public String solution(String myString) {
        String[] strArr = new String[myString.length()];
        
        for (int i = 0 ; i < myString.length() ; i++) {
            String ele = Character.toString(myString.charAt(i));
            if (ele.equals("a")) {
                strArr[i] = "A";
            } else if (!ele.equals("A") && Character.isUpperCase(myString.charAt(i))){
                strArr[i] = ele.toLowerCase();
            } else {
                strArr[i] = ele;
            }
        }
        
        String answer = String.join("", strArr);
        return answer;
    }
}