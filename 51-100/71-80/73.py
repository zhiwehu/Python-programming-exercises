"""
Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
请编写一个二分查找函数，用于搜索排序列表中的项目。函数应返回列表中要搜索的元素的索引。


Hints:
提示：
Use if/elif to deal with conditions.
使用if/eif处理条件。
"""
# 本人答案
def search(n,tas):
    tas.sort()
    low = 0
    high = len(tas) - 1
    while low <= high:
        mid = (low + high) // 2
        if tas[mid] == n:
            return mid
        elif tas[mid] < n:
            low = mid + 1
        else:
            high = mid - 1
    return -1

li=[2,5,7,9,11,17,222]
print (search(li,11))
print (search(li,12))