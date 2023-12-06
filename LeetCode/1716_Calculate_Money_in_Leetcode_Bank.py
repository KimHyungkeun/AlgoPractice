# https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/?envType=daily-question&envId=2023-12-06

class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        num_list = [1,2,3,4,5,6,7]

        for i in range(n) :
            total += (num_list[i % 7] + i // 7)
        
        return total