__author__ = 'willard'
#-*- coding: utf-8 -*-
from xlrd import open_workbook
import os
import math
import sys
import re
import string
import shutil

def main():
    header = 'const byte PY_mb_'
    src = open('new.txt', 'r')
    dest = open('output.txt', 'w')

    isFirstLine = 0
    word = ''
    aline = src.readline()
    while aline:
        pinyin = aline.split('\t')[1]
        if (isFirstLine == 0):
            pinyin_last = pinyin
            isFirstLine = 1

        if (pinyin != pinyin_last):#不是同一个拼音，需要写入一行
            temp = pinyin_last[:-1] + '[]' + (10-len(pinyin_last[:-1]))*' '
            dest.write(header+temp+'={"'+word+'"};\n')
            word = ''

        pinyin_last = pinyin
        word += aline.split('\t')[0]
        aline = src.readline()

    temp = pinyin_last[:-1] + '[]' + (10-len(pinyin_last[:-1]))*' '
    dest.write(header+temp+'={"'+word+'"};\n')
    src.close()
    dest.close()

if __name__ == '__main__':
	main()