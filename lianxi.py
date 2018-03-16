# nums = [x for x in range(10)]
#
# print(nums)

# a = [x for x in range(1,101)]
# print(a)
# b = [ a[x:x+3] for x in range(0,len(a),3)]
# print(b)

# a[x:x+3]
a = [1,]
b = [a[x:x+3] for x in range(0,len(a),3)]
print(b)

