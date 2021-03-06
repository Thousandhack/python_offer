#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "hsz"

"""
选择排序
选择排序是一种简单直观的排序算法，无论什么数据进去都是 O(n²) 的时间复杂度。所以用到它的时候，数据规模越小越好。唯一的好处可能就是不占用额外的内存空间了吧。
1. 算法步骤
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
重复第二步，直到所有元素均排序完毕。
"""


def select_sort(list_demo):
    n = len(list_demo)
    for j in range(n - 1):
        min_index = j
        for i in range(j + 1, n):
            if list_demo[min_index] > list_demo[i]:
                min_index = i
        list_demo[j], list_demo[min_index] = list_demo[min_index], list_demo[j]


if __name__ == "__main__":
    li = [7, 9, 3, 5, 1]
    print(li)
    select_sort(li)
    print(li)
