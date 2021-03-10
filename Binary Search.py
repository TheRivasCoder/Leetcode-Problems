numbers = [-1,0,3,5,9,12]
target = 5
def search(nums, target): #use binary search solution
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    Left = 0 #Left pointer is first item in list
    Right = len(nums)-1 #Right pointer is last item in list
    while Left<=Right: #continue search while Left and Right pointers move towards each other
        middle = (Left+Right)//2 #middle is found by adding Left and Right pointers to each other and dividing by two
        if nums[middle] < target:
            Left = middle +1
        elif nums[middle] > target:
            Right = middle -1
        elif nums[middle] == target: #checking if middle is equal to target or if either pointer should move to middle
            return middle
    return -1 #return -1 if target not found
print(search(numbers, target))