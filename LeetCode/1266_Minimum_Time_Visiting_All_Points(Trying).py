# https://leetcode.com/problems/minimum-time-visiting-all-points/?envType=daily-question&envId=2023-12-06
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        cnt = 0
        if len(points) == 1 :
            return cnt

        for i in range(len(points)-1) :
            start = points[i]
            target = points[i+1]

            if abs(start[0] - target[0]) == 0 :
                cnt += abs(start[1] - target[1])
            
            elif abs(start[1] - target[1]) == 0 :
                cnt += abs(start[0] - target[0])
            
            elif abs(start[0] - target[0]) < abs(start[1] - target[1]) :
                cnt += abs(start[0] - target[0])
                if start[0] < target[0] :
                    tmp = start[1] + cnt
                    cnt += abs(tmp - target[1])
                else :
                    tmp = start[1] - cnt
                    cnt += abs(tmp - target[1])


            elif abs(start[0] - target[0]) > abs(start[1] - target[1]) :
                cnt += abs(start[1] - target[1])
                if start[1] < target[1] :
                    tmp = start[0] + cnt
                    cnt += abs(tmp - target[0])
                else :
                    tmp = start[0] - cnt
                    cnt += abs(tmp - target[0])

            else :
                cnt += abs(start[0] - target[0])
            
            print(cnt)

            
        return cnt