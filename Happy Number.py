		
        
visited = set()
while n!=1:
    sum = 0
    n = str(n)
    for char in n:
        sum += int(char)**2
    if sum in visited:
        return False
    visited.add(sum)
    n = sum
return True