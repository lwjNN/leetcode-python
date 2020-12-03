# sum = lambda arg1, arg2: arg1 + arg2
# print("Value of total : %d" % sum(10, 20))
# print("sum=%d" % sum(10, 20))


def fun(a, b, opt):
    print("a= %d" % a)
    print("b= %d" % b)
    print("result=%d" % opt(a, b))


fun(1, 2, lambda x, y: x + y)

stus = [
    {"name": "zhangsan", "age": 18},
    {"name": "lisi", "age": 20},
    {"name": "wangwu", "age": 10},
]

stus.sort(key=lambda x:x["name"])
print(stus)

stus.sort(key=lambda x:x["age"])
print(stus)