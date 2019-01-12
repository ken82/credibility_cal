#!/usr/local/bin/python3
#_*_coding:utf-8_*_
# Database操作全般に関するプログラム(sqlite3)
import sqlite3

# DB内の特定データの検索(テーブル名と検索キーワードを受け取る)
def search(table_name, keyword):
    db = sqlite3.connect('./database/credibility_assessment.db')  # DBに接続
    query = "select * from " + table_name + " where data like ?"  # クエリ
    cmd = db.execute(query,('%' + keyword + '%',))  # SQLの実行
    return cmd
    db.close()  # データベースとの接続解除



# ディレクトリ内のjsonを取得して特定のデータを取り出しdbに保存
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
