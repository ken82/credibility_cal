#!/usr/local/bin/python3
#_*_coding:utf-8_*_
#Twitterから情報収集．credibility_cal.pyで前処理したデータを受け取り実行．ターゲットの共起情報を抽出しデータベスに格納するプログラム
import re
import json
import random
import tweepy
import sqlite3
import preprocessing
import datetime, time, sys
from requests_oauthlib import OAuth1Session

def cotw(target_i):
    judge_result = (preprocessing.judge_lang(target_i))  # 言語判定モジュールを実行
# TwitterAPI情報
    ck = "ZgAphA1TIhWNzak1JCnybEGgl"  # CONSUMER_KEY
    cs = "Vc6t2wjRdoUaIIfii4LqsHEh164DJXcI6KzzwO5DuNEJc6byWp"  # CONSUMER_SECRET
    at = "1065651864505446400-Suv0xkvXqj4SZIUppNHTEbmstU0NgG"  # ACCESS_TOKEN
    ats = "JvDt5a958hgzGhAjjehrh569kWQxECq8Vkq8j447Mvc7E"  # ACCESS_TOKEN_SECRET
# 認証
    session = OAuth1Session(ck, cs, at, ats)
    auth = tweepy.OAuthHandler(ck, cs)
    auth.set_access_token(at, ats)
    api = tweepy.API(auth)

# 共起情報の取得----------------------------------------------------------------
    q = target_i
    date = []  # ツイートの時刻を格納するリスト
    tweets_data = []  # ツイートのデータを格納していくリスト
    dataset = []  # 上の二つを統合するリスト
    
    # 100件までのツイートを取得
    if judge_result == "English":  # もし英語なら
        tweet = api.search(q, count=100)  # ツイートを取得(APIの仕様なのか英語だとRT除外するとエラーになる)
    elif judge_result == "Japanese":  # もし日本語なら
        tweet = api.search(q+"exclude:retweets", count=100)  # RTを除外してツイートを取得

# データベース操作
    db = sqlite3.connect('./database/credibility_assessment.db')  # sqlite dbへ接続
    db.execute("drop table twitter_data")  # 毎回dbをリセットするためにドロップ
    db.execute("create table twitter_data(id integer primary key, clock integer, data text)")  # dbを再構築

# 取得した共起情報の日付とテキストを順次データベースへ格納
    for tweets in tweet:
        date = str(tweets.created_at)  # 取得したツイートのタイムスタンプを格納していく
        #tweets_data = tweets.text
        raw_data = tweets.text  # 取得したツイートのテキストを取得
        tweets_data = preprocessing.cleansing(raw_data)  # 正規表現によるテキストのクリーニングのモジュールを実行
        dataset = [date, tweets_data]  # dbにいれるためにセットにする
        print(dataset)  # 抽出した共起情報を画面に表示する
        print("<br><br>")  # 見やすくするため改行
        db.execute("insert into twitter_data (clock, data) values (?,?)", dataset)  # dbにinsert
# データベースへの反映と接続解除
    db.commit()  # 変更をデータベースに保存
    db.close()  # データベースとの接続解除
    return "<br>"

# 参考URL
# Twitter Developer(https://developer.twitter.com/en/apps/15989011)
# https://qiita.com/kngsym2018/items/2524d21455aac111cdee