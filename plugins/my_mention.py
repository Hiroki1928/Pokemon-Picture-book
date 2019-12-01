# -*- coding: utf-8 -*-

from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ
import sys
import random
import os
os.chdir(os.path.dirname(__file__))

sys.path.append('../plugins')
from list_load import search_exec_string
from list_load import search_exec_num

@default_reply()
def default_func(message):
    text = message.body['text']     # メッセージを取り出す
    # 送信メッセージを作る。改行やトリプルバッククォートで囲む表現も可能
    # msg = 'あなたの送ったメッセージは\n```' + text + '```'
    if 'ポケモン' in text:
        no = random.randint(1,151)
        msg = search_exec_num(no)
    else:
        msg = search_exec_string(text)
    message.reply(msg)