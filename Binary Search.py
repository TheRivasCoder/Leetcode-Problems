class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        Left = 0
        Right = len(nums)-1
        while Left<=Right:
            middle = (Left+Right)//2
            if nums[middle] < target:
                Left = middle +1
            elif nums[middle] > target:
                Right = middle -1
            elif nums[middle] == target:
                return middle
        return -1