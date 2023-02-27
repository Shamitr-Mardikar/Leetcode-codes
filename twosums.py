class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        for i, j in enumerate(nums):  #Enumerate function converts the list into a key:value format
            r = target - j #instead of checking num1+num2 = target; it checks target-num1=num2?
            if r in d: return [d[r], i]
            d[j] = i