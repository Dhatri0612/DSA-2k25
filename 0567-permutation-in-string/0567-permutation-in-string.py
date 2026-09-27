class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        l1=list(s1)
        l2=list(s2)
        k=len(l1)
        window=l2[:k]
        for right in range(k,len(l2)):
            if sorted(l1)==sorted(window):
                return True
            del window[0]
            window.append(l2[right])
            left+=1
        if sorted(l1)==sorted(window):
            return True
        return False