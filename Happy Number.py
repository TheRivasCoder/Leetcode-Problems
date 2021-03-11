

def isHappy(n):      
    visited = set()
    while n!=1: # create loop to check if n ever becomes 1
        sum = 0
        n = str(n)
        for char in n:
            sum += int(char)**2 # squares all digits in n and adds them to sum
        if sum in visited: # check if new sum has been encountered before to see if we are in an endless loop
            return False
        visited.add(sum)
        n = sum # changes n to new sum to check again if it is equal to 1 and we can return True
    return True



print(isHappy(2))
print(isHappy(3))
print(isHappy(4))
print(isHappy(5))
print(isHappy(6))
print(isHappy(7))