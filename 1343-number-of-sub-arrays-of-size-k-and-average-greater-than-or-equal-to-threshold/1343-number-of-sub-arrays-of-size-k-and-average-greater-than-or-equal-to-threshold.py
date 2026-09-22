class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        left=0
        window_sum=sum(arr[:k])
        window_avg=sum(arr[:k])//k
        count=0
        if window_avg>=threshold:
            count+=1
        for right in range(k,len(arr)):
            window_sum=window_sum-arr[left]+arr[right]
            left+=1
            window_avg=window_sum//k
            if window_avg>=threshold:
                count+=1

        return count