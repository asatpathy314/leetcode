class Solution:
    def intToRoman(self, num: int) -> str:
        numeral = ""
        if num > 999:
            numeral += "M" * (num // 1000)
            num -= 1000 * (num // 1000)
        if num > 899:
            numeral += "CM"
            num -= 900
        if num > 499:
            numeral += "D"
            num -= 500
        if num > 399:
            numeral += "CD"
            num -= 400
        if num > 99:
            numeral += "C" * (num // 100)
            num -= 100 * (num // 100)
        if num > 89:
            numeral += "XC"
            num -= 90
        if num > 49:
            numeral += "L"
            num -= 50
        if num > 39:
            numeral += "XL"
            num -= 40
        if num > 9:
            numeral += "X" * (num // 10)
            num -= 10 * (num // 10)
        if num == 9:
            numeral += "IX"
            num -= 9
        if num > 4:
            numeral += "V"
            num -= 5
        if num == 4:
            numeral += "IV"
            num -= 4
        if num > 0:
            numeral += "I" * num
            num -= num
        return numeral


"""
Above is the funny solution. Beats 100% of solutions in runtime.
Below is the real solution. Do not use the above in real interview or you're cooked.
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        cache = {
            1000: ("", "", "", "M"),
            100: ("CM", "D", "CD", "C"),
            10: ("XC", "L", "XL", "X"),
            1: ("IX", "V", "IV", "I"),
        }

        numeral = ""
        for base in [1000, 100, 10, 1]:
            while num // base > 0:
                div = num // base
                if div == 9:
                    numeral += cache[base][0]
                    num -= 9 * base
                elif div > 4:
                    numeral += cache[base][1]
                    num -= 5 * base
                elif div == 4:
                    numeral += cache[base][2]
                    num -= 4 * base
                else:
                    numeral += cache[base][3]
                    num -= base
        return numeral
