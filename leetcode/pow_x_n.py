"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]

"""


class Solution(object):

    def my_pow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        bin_n = bin(abs(n))
        used = [int(x) for x in list(bin_n[2:])]
        used.reverse()
        print(used)
        result = 1
        current = x
        for yes in used:
            if yes:
                result *= current
            current *= current
            # print(result, current)
        if n < 0:
            return 1 / result
        return result
