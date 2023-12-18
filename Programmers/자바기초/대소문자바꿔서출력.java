import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        for (int i = 0 ; i < a.length(); i++) {
            if (97 <= (int)a.charAt(i) && (int)a.charAt(i) <= 122) {
                int answer = (int)a.charAt(i) - 32;
                System.out.print((char)answer);
            } else {
                int answer = (int)a.charAt(i) + 32;
                System.out.print((char)answer);
            }
        }
    }
}