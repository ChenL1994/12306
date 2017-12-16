from ticket.info import *
from ticket.out import *
import ticket.prompt.speak as speak
import time
import datetime


# dsts = [
#     "2017-12-22",
#     "2017-12-23",
# ]
today = datetime.datetime.now()  # 今天
dsts = [  # 出行日期
    (today + datetime.timedelta(days=1)).strftime("%Y-%m-%d"),  # 明天
    (today + datetime.timedelta(days=2)).strftime("%Y-%m-%d"),  # 后天
    (today + datetime.timedelta(days=3)).strftime("%Y-%m-%d"),  # 第三天
]
tps = [  # 票类型
    "硬卧",
    "硬座",
]
ast = "太原"  # 起点
aed = "重庆"  # 终点
sec = 5  # 每隔 5s 刷新一次

flag = True  # 无票标志
while 1:
    for dst in dsts:
        try:
            for i in getInfo(ast, aed, dst):
                for tp in tps:
                    target = items.index(tp)
                    if i[target] != "-" and i[target] != "无" and i[target] != "":
                        print(out([dst, ] + i[:6] + [i[target], tp], 12))
                        speak.say()  # 有票提醒
                        flag = False
        except Exception as e:
            print(e)
    if flag:
        print("还没有票，等待中......")
        time.sleep(sec)
    else:
        # 有票了
        break
