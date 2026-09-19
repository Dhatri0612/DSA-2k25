class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict={}
        reverse={}
        for i in range(len(s)):
            if s[i] not in dict and t[i] not in reverse:
                dict[s[i]]=t[i]
                reverse[t[i]]=s[i]
            elif dict.get(s[i])==t[i] and reverse.get(t[i])==s[i]:
                continue
            else :
                return False
        return True