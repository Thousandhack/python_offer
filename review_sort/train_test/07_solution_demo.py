#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

"""
反转一个整数，例如-123 --> -321
"""


class Solution(object):

    def int_reverse(self, x):
        if -10 < x < 10:
            return x
        str_x = str(x)
        if str_x[0] != "-":
            str_x = str_x[::-1]

            x = int(str_x)
        else:
            str_x = str_x[1:][::-1]
            x = int(str_x)
            x = -x
        return x if -2147483648 < x < 2147483647 else 0


if __name__ == '__main__':
    s = Solution()
    reverse_int = s.int_reverse(-123)
    print(reverse_int)
