# # 1 -- 100 奇数
# for i in range(101):
#     if i % 2 == 1:
#         print(i)
#  查找输入的文件名下的所有文件
# def print_directory_contents(sPath):
#     import os
#     for sChild in os.listdir(sPath):
#         sChildPath = os.path.join(sPath,sChild)
#         if os.path.isdir(sChildPath):
#             print_directory_contents(sChildPath)
#         else:
#             print(sChildPath)
# 1 到 100 的和
# i = 1
# sum1 = 0
# while i <= 100:
#     sum1 = sum1 + i
#     print('he wei %d'%sum1)
#     i +=1
# 打印星星
# i = 1
# while i <=5:
#     j = 1
#     while j <= i:
#         print('*',end='')
#         j += 1
#     print()
#     i += 1

# 偶数的和
# i = 1
# a = 0
# while i <= 100:
#     if i % 2 == 0:
#         a = a +i
#     i += 1
# print(a)

# 打印乘法表
# i = 1
# while i <= 9:
#     j = 0
#     while j <= i:
#         print("%d*%d=%2d"%(j,i,i*j),end='')
#         j += 1
#     print("\n")
#     i += 1

# index = 0
# while index < 10:
#     if index >7:
#         break
#     else:
#         print(index,end='')
#     index += 1
# print()
# 1 - 100 的奇数
# a = [x for x in range(101) if x % 2 != 0]
# print(a)
#  使用装饰器使输入的文件名首字母大写
# import functools
#
#
# def outside(func):
#     @functools.wraps(func)
#     def inner():
#         ret = func()
#         print(ret.title())
#     return inner
#
#
# @outside
# def greetings(word='hi there'):
#     return word.lower()
#
# greetings()

#  斐波那契数列
# fibs = [0,1]
# num = input('ni shu ru de shu zi wei:')
# for i in range(int(num)-2):
#     fibs.append(fibs[-2]+fibs[-1])
# print(fibs)

