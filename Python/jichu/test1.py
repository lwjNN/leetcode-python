import keyword
"""
多行注释
"""

print(8//3)
print(8**3)
print("*" * 20)
print(True+1)
print(type(True+1))

print(keyword.kwlist)

# var = input("请输入：")
# print(var)

price = float(input("请输入价格："))
count = float(input("请输入数量"))
money = price * count
print(money)