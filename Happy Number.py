		


class Solution:
    def isHappy(self, n: int) -> bool:       
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

check_if_happy = Solution()

print(check_if_happy.isHappy(2))
print(check_if_happy.isHappy(3))
print(check_if_happy.isHappy(4))
print(check_if_happy.isHappy(5))
print(check_if_happy.isHappy(6))
print(check_if_happy.isHappy(7))