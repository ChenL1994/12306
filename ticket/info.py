"""
 3：车次
 4：出发站（代码map["data"]["map"]）
 5：终点站（代码）
 6：出发站，过站（代码）
 7：终点站，过站（代码）
 8：出发时间
10：历时
 9：到达时间
32：商务座特等座
31：一等座
30：二等座
21：高级软卧
23：软卧
33：动卧
28：硬卧
27：软座
29：硬座
26：无座
"""

import requests
import json
import datetime
from .data import area

items = (
    "车次",
    "起点",
    "终点",
    "出发时间",
    "历时",
    "到达时间",
    "商务座特等座",
    "一等座",
    "二等座",
    "高级软卧",
    "软卧",
    "动卧",
    "硬卧",
    "软座",
    "硬座",
    "无座",
)


def getInfo(ast, aed, dst=""):
    if dst == "":
        i = datetime.datetime.now()
        dst = i.strftime("%Y-%m-%d")
    url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT" % (dst, area[
                                                                                                                                                                    ast], area[aed])
    js = json.loads(requests.get(url).text)
    dt = js["data"]
    res = dt["result"]
    kvmap = dt["map"]
    for i in res:
        il = i.split("|")
        ylt = [
            il[3],  # 车次 0
            kvmap[il[4]] if il[4] in kvmap else kvmap[il[6]],  # 出发站 1
            kvmap[il[5]] if il[5] in kvmap else kvmap[il[7]],  # 下车站 2
            il[8],  # 出发时间 3
            il[10],  # 历时 4
            il[9],  # 到达时间 5
            il[32],  # 商务座特等座 6
            il[31],  # 一等座 7
            il[30],  # 二等座 8
            il[21],  # 高级软卧 9
            il[23],  # 软卧 10
            il[33],  # 动卧 11
            il[28],  # 硬卧 12
            il[27],  # 软座 13
            il[29],  # 硬座 14
            il[26],  # 无座 15
        ]
        yield ylt
