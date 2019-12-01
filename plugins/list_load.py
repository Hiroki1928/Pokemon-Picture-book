# -*- coding: utf-8 -*-

import xlrd
import os
os.chdir(os.path.dirname(__file__))

# ファイルの読み込み
# ファイルパスは端末ごとに指定
wb = xlrd.open_workbook('List.xlsx')

# 読み込むシートの指定
sheet = wb.sheet_by_name('Sheet1')

def search_exec_string(input_text):
    exec_list = search_list_make()
    exec_int = list_search(exec_list, input_text)
    if exec_int == 'None':
        return '見つかりませんでした'
    else:
        exec_match = match_output(exec_int)

    # アウトプット文字列の整形
    exec_ouput = '\nNo.{0[0]:.0f} {0[1]}({0[2]})\n{0[3]}\n高さ：{0[4]}m 重さ：{0[5]}kg\nタイプ１： {0[6]}\nタイプ２：{0[7]}'.format(exec_match)
    return exec_ouput

def search_exec_num(input_number):
    exec_match = match_output(input_number)

    # アウトプット文字列の整形
    exec_ouput = '\nNo.{0[0]:.0f} {0[1]}({0[2]})\n{0[3]}\n高さ：{0[4]}m 重さ：{0[5]}kg\nタイプ１： {0[6]}\nタイプ２：{0[7]}'.format(exec_match)
    return exec_ouput

def search_list_make():
    # 検索対象のリスト化
    search_list = sheet.col_values(1)
    return search_list

def list_search(list, search_word):
    for i in range(len(list)):
        if search_word == list[i]:
            return i
    return 'None'

def match_output(search_hit):
    # 出力対象のリスト化
    hit = sheet.row_values(search_hit)
    return hit