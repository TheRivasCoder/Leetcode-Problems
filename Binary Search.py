numbers = [-1,0,3,5,9,12]
target = 13
def search(nums, target):
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
print(search(numbers, target))