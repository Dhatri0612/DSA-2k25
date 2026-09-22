class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l=list(s)
        count= 0
        for ch in l[:k]:
            if ch in'aeiou':
                count+=1
        max_count=count
        for right in range(k,len(l)):
            if l[right-k] in 'aeiou':
                count-=1
            if l[right] in 'aeiou':
                count+=1
            max_count=max(count,max_count)
        return max_count