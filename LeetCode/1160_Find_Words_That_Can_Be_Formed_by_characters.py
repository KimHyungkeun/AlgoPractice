# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/?envType=daily-question&envId=2023-12-06
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        keyword = {}
        cnt = 0
        for c in chars :
            if c not in keyword :
                keyword[c] = 1
            else :
                keyword[c] += 1
        

        for ele in words :
            tmp_key = {}
            for w in ele :
                if w not in tmp_key :
                    tmp_key[w] = 1
                else :
                    tmp_key[w] += 1
            
            flag = True
            for key in tmp_key.keys() :
                if key not in keyword :
                    flag = False
                    break
                else :
                    if tmp_key[key] > keyword[key] :
                        flag = False
                        break
            if flag :
                cnt += len(ele)

        return cnt