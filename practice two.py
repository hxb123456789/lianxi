# def factorl(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorl(n-1)
#
# b = factorl(10)
# print(b)

# def factorl(x,n):
#     if n == 0:
#         return 1
#     else:
#         return x * factorl(x,n-1)
#
# b = factorl(2,3)
# print(b)
#
# def search(sequence,number,lower,upper):
#     if lower == upper:
#         assert number == sequence[upper]
#         return upper
#     else:

import time

start_time = time.time()

# 注意是三重循环
for a in range(0, 1001):
    for b in range(0, 1001):
        c = 1000 - a - b
        if a**2 + b**2 == c**2 :
            print("a, b, c: %d, %d, %d" % (a, b, c))

end_time = time.time()
print("elapsed: %f" % (end_time - start_time))
print("complete!")



