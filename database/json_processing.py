#!/usr/local/bin/python3
#_*_coding:utf-8_*_
# データの処理全般を行うためのプログラム
import json
import sqlite3

path = input()  # dataset/germanwingsにあるデータ識別IDを入力する
# jsonファイルから特定のデータを抽出しdbに格納する
def data_processing(path):
    db = sqlite3.connect('./credibility_assessment.db')  # dbへ接続
    json_file = "./../dataset/germanwings-crash/rumours/" + path + "/source-tweet/"+ path + ".json"  # JSONファイルのパスを指定
    json_data = json.load(open(json_file))  # jsonファイルを開く
# jsonデータの処理
    json_time = json_data["created_at"]  # jsonデータ内の時間(created_at)を取得
    json_text = json_data["text"]  # jsonデータ内の本文を取得
    json_dataset = [json_time, json_text]  # 取得したjsonデータの時間と本文をセットにする
    db.execute("insert into rumor_germanwings(time, data) values (?,?)", json_dataset)  # セットした json_dataset を db にinsert
    db.commit()  # 変更をデータベースに保存
    db.close()  # データベースとの接続解除
data_processing(path)