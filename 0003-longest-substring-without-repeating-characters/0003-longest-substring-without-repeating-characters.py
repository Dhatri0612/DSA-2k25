class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=list(s)
        seen=set()
        left=0
        max_len=0
        for right in range(len(l)):
            while l[right] in seen:
                seen.remove(l[left])
                left+=1
            length= right-left+1
            seen.add(l[right])
            max_len=max(length,max_len)
        return max_len