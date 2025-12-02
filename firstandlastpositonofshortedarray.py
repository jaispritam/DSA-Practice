#34. Find First and Last Position of Element in Sorted Array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums)
        while left < right:
            mid = (right + left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid 
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]
        first = left

        left, right = 0, len(nums)
        while left < right:
            mid = (right + left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid 
        second = left - 1 
        return [first, second]