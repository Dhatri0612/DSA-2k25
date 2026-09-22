class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        window_sum=0
        size = float('inf')
        for right in range(len(nums)):
            window_sum+=nums[right]
            while window_sum>=target:
                current_size=right-left+1
                size=min(current_size,size)
                window_sum-=nums[left]
                left+=1
        if size == float('inf'):
            return 0

        return size