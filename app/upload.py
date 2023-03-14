# encoding:utf-8
import os, sys
from datetime import datetime


# ----gtj 用于上传文件的文件名修改
def change_filename(filename):
    dt = datetime.now()
    time = dt.strftime('%Y%m%d%H%M%S')
    filename = time + filename
    return filename


def percentage(consumed_bytes, total_bytes):
    if total_bytes:
        rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
        print('\r{0}% '.format(rate), end='')
        sys.stdout.flush()

