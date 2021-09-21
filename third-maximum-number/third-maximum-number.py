class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=set(nums)
        nums=list(nums)
        nums=sorted((nums),reverse=True)
        print(nums)
        if len(nums) < 3:
            return nums[0]
        else:
            return nums[2]
        
        
    # If we want to  reduce lines of code:

        # nums = sorted(list(set(nums)), reverse = True)
        # return nums[0] if len(nums) < 3 else nums[2]