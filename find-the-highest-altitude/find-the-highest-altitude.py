class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum_c = 0
        max_h = 0
        for i in gain:
            sum_c = sum_c + i
            max_h = max(sum_c, max_h)
        return max_h