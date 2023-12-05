class Solution:
    def numberOfMatches(self, n: int) -> int:
        cnt = 0
        while n != 1 :           
            cnt += (n // 2)         

            if n % 2 == 0 :
                n //= 2
            else :
                n //= 2
                n += 1
            print(cnt)

        return cnt
        