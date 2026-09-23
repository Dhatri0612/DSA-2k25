class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left=0
        count={}
        max_len=0
        for right in range(len(fruits)):
            count[fruits[right]]=count.get(fruits[right], 0) + 1
            while len(count)>2:
                count[fruits[left]] -= 1
                if count[fruits[left]] ==0:
                    del count[fruits[left]]
                left+=1
            current_length = right - left + 1
            max_len = max(max_len, current_length)

        return max_len