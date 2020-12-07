from numpy import long


def concatenatedBinary(n: int) -> int:
    str = ""
    for i in range(1,n+1):
        str += bin(i)[2:]
    res = int(str, 2)%1000000007
    return res

print(concatenatedBinary(12))