class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum=sum(nums[:k])
        window_avg=window_sum/k
        avg=window_avg
        for right in range(k,len(nums)):
            window_sum=window_sum-nums[right-k]+nums[right]
            window_avg=window_sum/k
            avg=max(avg,window_avg)
        return avg