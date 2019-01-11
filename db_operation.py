#!/usr/local/bin/python3
#_*_coding:utf-8_*_
# Database操作全般に関するプログラム(sqlite3)
import sqlite3

# DBに値を格納する(テーブル名と値を引数にとる)
# def store(table_name, value):
#     db = sqlite3.connect('./database/credibility_assessment.db')  # DBに接続
#     sql = "insert into", table_name, "(clock, data) values (?,?)", value)  # DBに受け取った値を格納
#     db.execute(sql)  # SQLの実行
#     db.commit()  # 変更をデータベースに保存
#     db.close()  # データベースとの接続解除
#     return "success!"

# DB内の特定データの検索
def search(table_name, keyword):
    db = sqlite3.connect('./database/credibility_assessment.db')  # DBに接続
    sql = "select * from rumor_germanwings where data like '%" + keyword + "%'" # DB内を特定キーワードで検索
    #db.execute(sql)  # SQLの実行
    information = db.execute(sql)
    db.commit()  # 変更をデータベースに保存
    db.close()  # データベースとの接続解除
    return information
