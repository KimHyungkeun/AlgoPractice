class Solution:
    def largestGoodInteger(self, num: str) -> str:
        num_list = []
        for i in range(len(num)-2) :
            tmp = num[i:i+3]
            if tmp[0] == tmp[1] and tmp [1] == tmp[2] :
                num_list.append(tmp)
        
        num_list.sort(reverse=True)
        
        if not num_list :
            return ""
        else :
            return num_list[0]        