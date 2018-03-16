#  右边角标往左移动找到一个小于6的数 把值放到左边角标位置

#左边角标往右移动 找到一个大于6的数，把值放到右边角标的位置

# 左边 小于6 右边的大于6  左右角标相等时，把6 放到那个位置
def quick_sort(li,start,end):
    if start >= end:
        return
    #  左边角标
    left = start
    #  右边角标
    right = end
    #  中间人
    mid = li[left]
    while left < right:
        #  大于中间值  往左走  目的找小于mid 值
        while left < right and li[right] >= mid:
            right -= 1
        #  当循环结束right  指向的值小于 中间值
        li[left] = li[right]
        #  小于中间值 往右走    目的找大于 mid 值
        while left <right and li[left] <= mid:
            left += 1
        li[right] = li[left]
    #  执行结束 left =right

    li[left] = mid
    #   上面只是执行一次  进行递归
    quick_sort(li,start,left-1)
    quick_sort(li,left+1,end)



if __name__ == '__main__':
    l = [6,9,4,8]
    quick_sort(l,0,len(l)-1)
    print(l)


