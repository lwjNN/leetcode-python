# a = [x for x in range(3,4)]
# print(a)
#
# a = [x for x in range(2,10,2)]
# print(a)
#
# a = [x for x in range(1,100) if x % 2 == 0]
# print(a)

# a = [(x, y) for x in range(3) for y in range(3)]
# print(a)
#
# a = [x for x in range(1, 101)]
# b = [a[x:x + 3] for x in range(0, len(a), 3)]
# print (b)
#
# print(5//2)

# s = "leetcode"
# l = list(s)
# l.sort()
# print(l)
# res = []
# for i in l[:]:
#     res.append(l.pop())
# print(res)

l = [1,2,3,4 ,1,5]
print(l[:(len(l) -4)])
print(l[2:5])

list1 = [-2,3,9,7,8,9]
print(list1.index(9))
print( "最大值是%d,下标是%d" % (max(list1),list1.index(max(list1))) )
