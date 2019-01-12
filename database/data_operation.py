#!/usr/local/bin/python3
#_*_coding:utf-8_*_
# データの処理全般を行うためのプログラム(書き換えが必要)
import os
import json
import sqlite3

# ディレクトリの操作
def directory():
    # 探索するディレクトリを指定("./dataset")するとループ一回毎に中のディレクトリを取得しdirへ
    # その中のサブディレクトリをリストにしてsubdirへ, その下のファイルを全てfilesへ(今回はsubdirはない)
    for dir, subdir, files in os.walk("./dataset/rumors"):
        if dir == "./dataset/rumors/ottawa_shooting":  # 指定したディレクトリなら(germanwings_crash, ottawa_shooting, sydney_siege)
            for file_name in files:  # 中のファイルを取得していく(全てstrなので実際のデータではない)
                print(file_name)
    return "Success!"

# jsonデータの処理
def json_processing(file_name):
    json_file = file＿name  # JSONファイルを指定
    #json_file = "./dataset/rumors/ottawa_shooting" + file_name  # JSONファイルのパスを指定(パスを手動で入れる場合)
    json_data = json.load(open(json_file))  # jsonファイルを開く
    json_time = json_data["created_at"]  # jsonデータ内の時間(created_at)を取得
    json_text = json_data["text"]  # jsonデータ内の本文(text)を取得
    json_dataset = [json_time, json_text]  # 取得したjsonデータの時間と本文をセットにする
    print(json_dataset)
    return "Success!"

# db操作
def json_to_db(json_dataset):
    db = sqlite3.connect('./credibility_assessment.db')  # dbへ接続
    db.execute("insert into rumor_germanwings(time, data, source_id) values (?,?,?)", json_dataset)  # セットした json_dataset を db にinsert
    db.commit()  # 変更をデータベースに保存
    db.close()  # データベースとの接続解除
    return "Success!"

# ディレクトリ内のjsonを取得して特定のデータを取り出す
def dir_json_db():
    # 上の関数を組み合わせる
    for dir, subdir, files in os.walk("./dataset/rumors"):
        if dir == "./dataset/rumors/ottawa_shooting":
            for file_name in files:
                json_file = "./dataset/rumors/ottawa_shooting/" + file_name  # os.walkは中身を見るだけでアクセスするわけではないのでファイルにアクセスするためにはそのファイル名を指定する必要がある
                json_data = json.load(open(json_file))
                json_time = json_data["created_at"]
                json_text = json_data["text"]
                json_dataset = [json_time, json_text]
                db = sqlite3.connect('./credibility_assessment.db')
                db.execute("insert into rumor_ottawashooting(time, data) values (?,?)", json_dataset)
                db.commit()  # 変更をデータベースに保存
                db.close()  # データベースとの接続解除
    return "Success!"
#dir_json_db()
