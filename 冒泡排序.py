


def bubble_sort(li):
    n = len(li)
    for j in range(n-1):
        count = 0
        for i in range(n-1-j):
            # print(i)
            if li[i] > li[i+1]:
                li[i],li[i+1] = li[i+1],li[i]
                count += 1
        if count == 0:
            break






if __name__ == '__main__':
    l = [6,3,9,2,7]
    bubble_sort(l)
    print(l)

# [6,3,9,4,2]
def bubble_sort(li):
    n = len(li)
    # 确定冒泡排序的趟数 n - 1
    for j in range(n - 1): # 0 1 2 3

        count = 0
        # 冒泡排序一趟，把最大的一个数排到最右边
        for i in range(n - 1 - j): # 0 3 每一趟冒泡 比较的次数越来越少
            if li[i] > li[i + 1]:
                # 交换
                li[i], li[i + 1] = li[i + 1], li[i]
                count += 1
        # for循环结束时，如果没有交换过，证明已经有序，直接返回
        if count == 0:
            break

if __name__ == '__main__':
    l = [1,1,2,4,5,6]
    # 3, 6, 4, 2, 9
    # i = 3
    # 3,6,4,2,9
    # 3,4,2,6,9
    bubble_sort(l)
    print(l)
    # 最坏时间复杂度：O(n^2)
    # 最优时间复杂度：O(n)
    # 稳定性：稳定