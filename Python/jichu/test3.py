'''
if 的嵌套演练
'''

has_ticket = True
knife_length = 27

if has_ticket:
    if knife_length >= 20:
        print("不允许上车")
    else:
        print("安检通过")
else:
    print("不允许进门")
