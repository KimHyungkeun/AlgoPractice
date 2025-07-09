class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splited = s.split(" ")
        answer = 0
        for idx in range(len(splited)-1, -1 ,-1) :
            if splited[idx] :
                answer = len(splited[idx])
                break
        
        return answer