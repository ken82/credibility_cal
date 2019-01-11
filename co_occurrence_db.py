#!/usr/local/bin/python3
#_*_coding:utf-8_*_
# 実験用にDBから共起情報を抽出する．credibility_cal.pyで前処理したデータを受け取り実行．ターゲットの共起情報を抽出する
# プログラムは適宜書き換えが必要．
import re
import json
import random
import tweepy
import sqlite3
import preprocessing
import datetime, time, sys
from requests_oauthlib import OAuth1Session

# データベース操作
def codb(target_i):
    q = target_i  # ターゲット情報を取得
    db = sqlite3.connect('./database/credibility_assessment.db')  # sqlite dbへ接続
    sql = 'select * from rumor_germanwings_all like '%% _' word =' + q
    rows = db.execute(sql)
    
    
# データベースから接続解除
    db.close()  # データベースとの接続解除
    return rows

# 参考URL
# Twitter Developer(https://developer.twitter.com/en/apps/15989011)
# https://qiita.com/kngsym2018/items/2524d21455aac111cdee