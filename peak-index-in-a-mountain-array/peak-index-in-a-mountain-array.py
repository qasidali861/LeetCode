class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l=len(arr)
        i=0
        while(arr[i]<arr[i+1]):
            i+=1
        return i
        # return(arr.index(max(arr)))