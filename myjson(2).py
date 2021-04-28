#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


def print_name():
    print("I am myjson!")

# 程序主入口
if __name__ == "__main__":
    """解读字符串拼装成json写入文件，方便其他语言解析数据"""
    file_path = "json.txt"
    print(file_path)
    file_obj = open(file_path, "r", encoding='UTF-8')
    all_lines = file_obj.readlines()
    data = {}
    key_value = 0

    for line in all_lines:
        line_info = line.split(',')
        if line_info:
            info = {"name": line_info[0], "url": line_info[1].replace("\n", "")}
            # info['age'] = 10
            # info['age'] = 15
            # print(info['age'])
            # exit(-1)
            # print(type(info))
            data[key_value] = info
            key_value += 1
    file_obj.close()
    file = open('json1.json', 'w', encoding='utf-8')
    # file.write(data)
    # print(data, file=file)
    # exit(-1)

    json.dump(data, file, ensure_ascii=False)
