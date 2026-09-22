class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=list(s)
        seen=set()
        size=0
        left=0
        for right in range(len(l)):
            while l[right] in seen:
                seen.remove(l[left])
                left+=1
            seen.add(l[right])
            current_size=right-left+1
            size=max(size,current_size)
        return size
            