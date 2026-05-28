class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}
        for i,item in enumerate(nums):
            remaining = target-item
            if remaining in dictt:
                return [dictt[remaining],i]
            dictt[item] = i


        