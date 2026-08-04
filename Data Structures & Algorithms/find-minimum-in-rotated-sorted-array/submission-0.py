class Solution:
    def findMin(self, nums: List[int]) -> int:
        minn = nums[0]
        for num in nums:
            if num < minn:
                minn = num
        return minn
        