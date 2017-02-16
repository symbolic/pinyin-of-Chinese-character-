__author__ = 'willard'
#-*- coding: utf-8 -*-
from xlrd import open_workbook

def main():
    header = 'const byte PY_mb_'
    book = open_workbook('a.xls')
    dest = open('output.txt', 'w')

    isFirstLine = 0
    pinyin_last = ''
    word = ''
    for s in book.sheets():
        for row in range(s.nrows):
            pinyin = s.cell(row, 1).value
            if (isFirstLine == 0):
                pinyin_last = pinyin
                isFirstLine = 1
            if (pinyin != pinyin_last):
                temp = pinyin_last + '[]' + (10-len(pinyin_last))*' '
                dest.write(header+temp+'={"')
                dest.write(word)
                dest.write('"};\n')
                word = ''

            pinyin_last = s.cell(row, 1).value
            word += s.cell(row, 0).value.encode('gb2312')
            #经实验发现，gbk与gb2312生成的文件一样，
            #utf-8生产的文件较大

        temp = pinyin_last + '[]' + (10-len(pinyin_last))*' '
        dest.write(header+temp+'={"')
        dest.write(word)
        dest.write('"};\n')
        dest.close()

if __name__ == '__main__':
    main()