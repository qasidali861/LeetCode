class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            other_pair = target - nums[i]
            if (other_pair in dic):
                return(dic[other_pair], i)
            dic[nums[i]] = i
            
            