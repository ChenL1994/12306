"""
    全半角对其封装
"""


def isAsc(c):
    return ord(c) <= 176


def fmt(s, length=0):
    lc = 0  # 半角字符个数
    bc = 0  # 全角字符个数
    for ss in s:
        if isAsc(ss):
            lc += 1
        else:
            bc += 1
    if length <= lc + bc * 2:
        return s
    return s + ' ' * (length - 2 * bc - lc)


def out(arr, leng):
    rs = ""
    for i in arr:
        if i != "":
            rs += fmt(i, leng)
        else:
            rs += fmt("-", leng)
    return rs


def outln(arr, leng):
    return out(arr, leng) + "\n"
