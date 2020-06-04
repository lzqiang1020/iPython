# -*- coding: UTF-8 -*-

import xlrd
import json
import os
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

cols = []
def json2excel(jsfile, excfile):
    # 读取json数据
    a = 1
    if os.path.exists(jsfile):
        # 先用key值写表头
        with open(jsfile, 'r',encoding='utf8') as fp:
            # 先用key值写表头
            line = fp.readline()
            if not line:
                print("没有内容")
            else:
                # 每一行转换成字典类型
                jsdata = json.loads(line)
                # 用key值做标题
                for k in jsdata.keys():
                    if k not in cols:
                        cols.append(k)
                        ws.append(cols) # 标题
        # 写值
        with open(jsfile, 'r', encoding='utf8') as fp:
            # 循环写值
            while True:
                print('正在写入的行数%s：' % a)
                line = fp.readline()
                if not line:
                    break
        # 转换为python对象
        jsdata = json.loads(line)
        rowdata = []
        for col in cols:
            # 获取每一行key值对应的value值
            rowdata.append(jsdata.get(col))
            a += 1
            ws.append(rowdata) # 写行
        # ws.append(cols) # 标题
        # print('保存中')
    wb.save(excfile) # 保存

if __name__ == '__main__':
    jsfile = "./test.json"
    excfile = "./111.xlsx"
    json2excel(jsfile, excfile)

