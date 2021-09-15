class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        result = 0
        for item in d.items():
            if item[1] == 1:
                result += item[0]

        return result