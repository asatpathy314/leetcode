class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        num_even = num_odd = n // 2
        if n % 2 == 1:
            num_even += 1
        return (pow(5, num_even, mod) * pow(4, num_odd, mod)) % mod


"""
Combinatorical solution.

A digit in an even indice is "good" if it is an even digit (0, 2, 4, 6, 8)

A digit in an odd indice is "good" if it is a prime digit (2, 3, 5, 7)

That means every odd indice in the string can be 1 of 4 possibilities and
every even indice in the string can be 1 of 5 possibilities with no
restrictions and duplication allowed. That means it's a simple permutation
calculation of (5 ** num_even_indices * 4 ** num_od_indices). Finally
because this number can be too big they give us a mod we can use. That
allows us to use python's modular exponentiation (which is much more
efficient than regular exponentiation of large numbers in python). 
"""
