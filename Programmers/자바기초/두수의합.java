import java.math.*;
class Solution {
    public String solution(String a, String b) {
        BigInteger numA = new BigInteger(a);
        BigInteger numB = new BigInteger(b);
        
        BigInteger total = numA.add(numB);
        return total.toString();
    }
}


// 아래는 오답 및 runtime 에러
// import java.lang.*;
// class Solution {
//     public String solution(String a, String b) {

//         StringBuffer sb = new StringBuffer(a);        
//         String revA = sb.reverse().toString();
//         sb = new StringBuffer(b);        
//         String revB = sb.reverse().toString();
//         String result = "";
        
//         if (revA.length() < revB.length()) {
//             for (int i = 0 ; i < revB.length() - revA.length() ; i++) {
//                 revA += "0";
//             }
//         } else {
//             for (int i = 0 ; i < revA.length() - revB.length() ; i++) {
//                 revB += "0";
//             }
//         }
        
//         boolean isUp = false;
//         for (int i = 0 ; i < revA.length() ; i++) {
//             int valA = Integer.parseInt(Character.toString(revA.charAt(i)));
//             int valB = Integer.parseInt(Character.toString(revB.charAt(i)));
            
//             if (valA + valB < 10 && isUp) {
//                 if (valA + valB + 1 < 10) {
//                     result += String.valueOf(valA + valB + 1);
//                     isUp = false;
//                 } else {
//                     result += String.valueOf(valA + valB - 10 + 1);
//                     isUp = true;
//                 }           
//             } else if (valA + valB < 10 && !isUp) {
//                 result += String.valueOf(valA + valB);
//                 isUp = false;
//             } else if (valA + valB >= 10 && isUp) {
//                 result += String.valueOf(valA + valB - 10 + 1);
//                 isUp = true;
//             } else if (valA + valB >= 10 && !isUp) {
//                 result += String.valueOf(valA + valB - 10);
//                 isUp = true;
//             } else;
            
            
//             if (i == revA.length()-1 && isUp && valA + valB + 1 >= 10) {
//                 result += "1";
//             } 
            
//             if (i == revA.length()-1 && !isUp && valA + valB >= 10) {
//                 result += "1";
//             } 
            
//         }
        
//         String answer = "";
        
//         for (int i = result.length()-1 ; i >= 0 ; i--) {
//             answer += Character.toString(result.charAt(i));
//         }
        
//         return answer;
//     }
// }