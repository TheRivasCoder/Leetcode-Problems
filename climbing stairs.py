n = 6

def climbStairs(n): #function returns number of possible unique combinations of 1 and 2 step increments to climb number of stairs (n)
    if n == 1: #check base cases where n is equal to 1 or 2 stairs 
        return 1
    elif n == 2:
        return 2
    prev = 1 #previous is equal to 1 steps
    curr = 2 #current is equal to 2 steps
    for i in range(2,n): #for each step after the first 2, count possible combinations of steps
        temp = curr #temporary is equal current steps
        curr = prev + curr #current is equal to previous step plus current steps
        prev = temp #previous is equal to temporary/first current steps
    return curr #after adding possible current and previous steps, return final current steps as number of uique combinations of steps
print(climbStairs(n))