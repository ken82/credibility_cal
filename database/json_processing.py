#!/usr/local/bin/python3
#_*_coding:utf-8_*_
# データの処理全般を行うためのプログラム(書き換えが必要)
import os
import json
import sqlite3

# jsonファイルから特定のデータを抽出しdbに格納する
data_id = input("データidを指定してください．")  # dataset/germanwingsにあるデータ識別IDを入力する
data_id2 = input("データid 2を入力してください．")
source_id = 1  # 同じsourceかどうかを識別する
def data_processing(data_id):
# ディレクトリの操作(未実装)
    # for dir, subdir, files in os.walk("./../dataset/germanwings-crash/rumours"):  # パスを指定すると，カレントディレクトリ, サブディレクトリ, ファイルの順でリスト取得
    #     for file_name in files:  # ファイルを取得していく
    #         print(file_name)

# jsonデータの処理
    #json_file = "./../dataset/germanwings-crash/rumours/" + data_id + "/reactions/" + data_id2 + ".json"  # JSONファイルのパスを指定(手動で入力する場合)
    json_file = "./../dataset/germanwings-crash/rumours/" + data_id + "/source-tweet/" + data_id + ".json"  # JSONファイルのパスを指定(手動で入力する場合)
    #json_file = "./../dataset/germanwings-crash/rumours/" + "581546828954411008" + "/reactions/" + data_id2 + ".json"  # JSONファイルのパスを指定(手動で入力する場合)
    json_data = json.load(open(json_file))  # jsonファイルを開く
    json_time = json_data["created_at"]  # jsonデータ内の時間(created_at)を取得
    json_text = json_data["text"]  # jsonデータ内の本文を取得
    json_dataset = [json_time, json_text, source_id]  # 取得したjsonデータの時間と本文をセットにする
    print(json_dataset)

# db操作
    db = sqlite3.connect('./credibility_assessment.db')  # dbへ接続
    db.execute("insert into rumor_germanwings(time, data, source_id) values (?,?,?)", json_dataset)  # セットした json_dataset を db にinsert
    db.commit()  # 変更をデータベースに保存
    db.close()  # データベースとの接続解除'''
data_processing(data_id)