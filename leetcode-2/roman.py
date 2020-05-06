"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. 
The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, 
the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine,
which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4."""

# Roman ---> Integer
# How would i convert XI <-input
# X = 10
# I = 1
# 10 + 1 = 11 <-output
# V = 5
# III = 1+1+1 = 3
# suppose we get IV if we add 1 + 5 = 6 incorrect answer
# whenever the previous number is small than we need to subtract
# if XLIX
# 10 + 50 -2(10) + 1 + 10 -2(1)
# 49
# thinking need to store all the numbers in a dictionary

# dic {I:1, V:5, X:10, l:50, C:100, D:500, M:1000}
# need 2 pointers
# prev = 0 so we can take the previous number
# curr = 0
# total = 0
# loop through the given string
# assign current as first value
# for i in range(len(string):
# current = dic[String[i]]
# if current > previous which is checking if previous is smaller
# total = total + current - 2 * prev
# else total + = current
# prev = current after every iteration
# return total

# XLIV
#   PREV, CURR,  TOTAL
#    0      0       0
# 1) 10     10      10
# 2) 10     50      40
# 3) 50     1       40
# 4) 1      10      41

# TOTAL = 10 - 2 * 0
# Total = 10
# 10 + 50 - 2 * 10
# 60-20 = 40
# 40 + 1 = 41
# 41 + 10 - 2(1)
# 51 -2
# TOTAL = 49


class Solution:
    def romanToInt(self, s: str) -> int:

        dic = {
            'I': 1,
            'V': 5,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        total = 0
        current = 0
        previous = 0

        for i in range(len(s)):
            current = dic[s[i]]
            if current > previous:
                total = total + current - 2 * previous
            else:
                total += current

            previous = current

        return total

        '''' Time complexity is O(n) because it has to loop through the dictionary to compare each string'''
