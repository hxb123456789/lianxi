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
# def a(sPath):
#     import os
#     for sChild in os.listdir(sPath):
#         sChildPath = os.path.join(sPath,sChild)
#         if os.path.isdir(sChildPath):
#             a(sChildPath)
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
# a = [x for x in range(101) if x % 2 == 0]

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

# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print("%d*%d=%-2d"%(j,i,j*i),end='')
#         j += 1
#     print("\n")
#     i += 1
# a = "adkfajdk"
# b = a[::-1]
# print(b)
#
# 求质数
# for num in range(10,20):
#     for i in range(2,num):
#         if num%i == 0:
#             break
#     else:
#         print(num)
# chars = ['a','b','c','d']
# i = 0
# for chr in chars:
#     print('%d %s'%(i,chr))
#     i += 1
# chars = ['a','b','c','d']
# i = 0
# for i,chr in enumerate(chars):
#     print(i,chr)
#     i += 1

# def a(num):
#     if num >=1:
#         result = num * a(num-1)
#     else:
#         result = 1
#     return result
# c = a(3)
# print(c)

# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print("%d*%d=%2d"%(j,i,j*i),end="")
#         j +=1
#     print("\n+")
#     i += 1

#
# for num in range(100,200):
#     for i in range(2,num):
#         if num%i == 0:
#             break
#     else:
#         print(num)
#
# f = [0,1]
# num = input("ni shu ru de shu zi shi :")
# for i in range(int(num)-2):
#     f.append(f[-2] + f[-1])
# print(f)

# f = open("test.txt","w")
# f.write("hello world, i am huang")
# f.close()
# # 提示输入文件
# oldFileName = input("请输入要拷贝的文件名字：")
# # # 以读的方式打开文件
# oldFile = open(oldFileName,"rb")
# # # 提取文件的后缀
# fileFlagNum = oldFileName.rfind(".")
# # # 提取文件的后缀
# if fileFlagNum >0:
#     fileFlag = oldFileName[fileFlagNum:]
# newFileName = oldFileName[:fileFlagNum] + "fujian" + fileFlag
#
#
# # # 创建新文件
# newFile = open(newFileName,"wb")
# # # 把旧文件中的数据，一行一行的进行复制到新文件中
# for lineContent in oldFile.readlines():
#     newFile.write(lineContent)
#
# # # 关闭文件
# oldFile.close()
# newFile.close()
#  单列模式
# class A(object):
#     __instance = None
#
#     def __new__(cls, ):
#         if cls.__instance is None:
#             cls.__instance = object.__new__(cls)
#             return cls.__instance
#         else:
#             return cls.__instance
#
#     def __init__(self):
#         print("__init__")
#
#
# c = A()
# print(c)
#
# d = A()
# print(d)
# A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# A1 = range(10)
# print(A1)
# A2 = [i for i in A1 if i in A0]
# print(A2)


