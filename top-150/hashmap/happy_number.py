class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)
        is_cyclical = True

        while n != 1:
            temp = n
            n = 0

            while temp > 0:
                n += pow(temp % 10, 2)
                temp //= 10

            if n in seen:
                is_cyclical = False
                break

            seen.add(n)

        return is_cyclical


"""
Keep track of seen numbers, and once we repeat, we can just return False. Otherwise return True. 
"""
