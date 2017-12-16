from ticket.info import *
from ticket.out import *
from os import system


def main():
    dst = input("出发日期(eg.2018-01-03)：")
    ast = input("出发城市：")
    aed = input("到达城市：")
    # dst = "2018-01-03"
    # ast = "上海"
    # aed = "北京"
    txt = ""
    txt += outln(items, 13)
    for i in getInfo(ast, aed):
        txt += outln(i, 13)
    with open("res.txt", "w") as f:
        f.write(txt)
    system("res.txt")

if __name__ == '__main__':
    main()
