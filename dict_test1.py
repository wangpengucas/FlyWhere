#!/usr/bin/python
# -*- coding:utf-8 -*-
import csv
csv_reader = csv.reader(open('全国机场三字代码.csv', encoding='utf-8'))
Airport_dict = {}
for row in csv_reader:
    if row[0].strip() == '':
        continue
    Info_list = []
    Info_list.append(row[1])
    Info_list.append(row[2])
    Info_list.append(row[3])
    Airport_key = row[0]
    Airport_dict[Airport_key] = Info_list
for key in Airport_dict:
    print(key + ":" + Airport_dict[key][0]+ " " + Airport_dict[key][1] + " "+ Airport_dict[key][2])

print(Airport_dict)