class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 1. target이 이미 있을 때
        if target in nums :
            return nums.index(target)

        # 2. nums 리스트가 1개일때
        if len(nums) == 1 :
            if nums[0] <= target :
                return 1
            else :
                return 0


        # 3. nums 리스트가 여러개 일때
        for idx in range(1, len(nums)) :
            if nums[idx-1] <= target <= nums[idx] :
                return idx
        


        # 4. 주어진 target이 리스트 내 값 중 최소 또는 최대일때
        if target <= min(nums) :
            return 0
        else :
            return len(nums)
        