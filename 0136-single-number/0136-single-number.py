class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        dict={}
        for num in nums:
            if num not in dict:
                dict[num]=1
            else:
                dict[num]+=1
        for key,value in dict.items():
            if value==1:
                return key
        