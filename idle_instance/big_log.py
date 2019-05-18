#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@auther = 'Redheat'
@create = '2019/5/17 13:22'
@email = 'qjyyn@qq.com'
'''
'''
nginx大日志处理
'''
from os.path import getsize
import math
import time


def get_before_timestamp(days=3):
    return time.time() - days * 24 * 60 * 60


def get_critical_seek():
    with open(file_name) as f:
        seek_start = 0
        seek_end = file_size
        before_days_timestamp = get_before_timestamp(3)
        while True:
            f.seek(math.ceil((seek_end - seek_start) / 2 + seek_start))
            f.readline()
            line = f.readline()
            current_log_time = line.split("[")[-1].split("]")[0]
            timeArray = time.strptime(current_log_time, "%d/%b/%Y:%H:%M:%S %z")
            current_log_timestamp = int(time.mktime(timeArray))
            if current_log_timestamp < before_days_timestamp:
                seek_start = f.tell()
            else:
                if seek_end != f.tell():
                    seek_end = f.tell()
                else:
                    return seek_end


def get_data(file_name, seek):
    data = {}
    with open(file_name) as f:
        f.seek(seek)
        for line in f:
            ip = line.split()[0]
            data[ip] = data.get(ip, 0) + 1
    sort_data = sorted(data.items(), key=lambda item: item[1], reverse=True)
    return sort_data[:10]


if __name__ == "__main__":
    file_name = "/data/bak_data/adm.log"
    file_size = getsize(file_name)
    current = time.time()
    seek = get_critical_seek()
    print(get_data(file_name, seek))
