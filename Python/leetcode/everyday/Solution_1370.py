def sortString(s: str) -> str:
    num = [0] * 26
    for c in s:
        num[ord(c) -ord('a')] += 1

    ret = []
    while len(ret) <len(s):
        for i in range(26):
            if num[i]:
                ret.append(chr(i + ord('a')))
                num[i] -= 1
        for j in range(25,-1,-1):
            if num[j]:
                ret.append(chr(j + ord('a')))
                num[j] -= 1

    return "".join(ret)


print(sortString("leetcode"))