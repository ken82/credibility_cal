#!/usr/local/bin/python3
#_*_coding:utf-8_*_
# NLPによりMatrix Node Graphを生成する
import os,sys,re
import json
import pprint
import pandas
import sklearn
import sqlite3
import numpy as np
import time, datetime
import preprocessing
# Intension Matrix(意図を分類するための二次元配列) 
'''x軸=意図, y軸=カテゴリ
Intension = [
[                "Anxiety(不安)", "agitation(扇動)", "Publicity(広告)", "Fun(愉快)", "Desire(願望)", "Admire(賞賛)","Obligation(義務)", "Politics(政治)"],
["Disaster(災害) ",   0,               0,                0,               0,             0,             0,              0,                0],
["Accident(事故) ",   0,               0,                0,               0,             0,             0,              0,                0],
["Terrorism(テロ)",   0,               0,                0,               0,             0,             0,              0,                0],
["Medical(医療)  ",   0,               0,                0,               0,             0,             0,              0,                0],
["Society(社会)  ",   0,               0,                0,               0,             0,             0,              0,                0],
["Politics(政治) ",   0,               0,                0,               0,             0,             0,              0,                0],
]
Intension Matrixの実態は上の形の行列だが実際には 0 のセルだけを作成'''
#target_i = input()  # 確認用
def mng(target_i):
    judge_result = (preprocessing.judge_lang(target_i))  # 言語判定モジュールを実行
    targets = target_i.split()  # ターゲット情報を空白で区切ってリストにする
    # ターゲット情報に対して意図分類を行いマトリクスを生成--------------------------------------------------------------------------
    # 上の行列と同じ構造を持つ意図分類マトリクスを生成
    target_intension = np.array([
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]])
 
    # NLPによる意図マトリクスの分類-----------------------------------------------------------------------------------------------
    # 辞書(json)の取得と処理
    dict_category = "./dict/category.json"  # カテゴリに関する固有表現辞書(gazetteer:ガゼッティアとも言う)
    dict_intension = "./dict/intension.json"  # 同じく意図に関する辞書
    category = json.load(open(dict_category, encoding='utf-8'))  # カテゴリのjsonを開きdict型に変換(日本語が含まれるのでエンコード)
    intension = json.load(open(dict_intension, encoding='utf-8'))  # 同じく意図のjsonを開く
    
    # パターンマッチング(カテゴリ)
    category_match = {}  # パターンマッチの結果を格納するリスト
    for categories in category.keys():  # カテゴリ名を取得
        category_text = list(category.get(categories))  # そのカテゴリ内の単語を取得
        category_type = set(category_text) & set(targets)  # カテゴリ内の単語とターゲット情報で一致するものを抽出
        category_count = len(list(category_type))  # set型になっているのでリストに変換しマッチした数を格納
        if category_count != 0:  # カテゴリとの一致数が0でなければ
            category_match.update({categories:category_count})  # 特定のカテゴリにマッチした数をそのカテゴリ名と共に格納
    print(category_match)
    print("<br><br><br>")
    # パターンマッチング(意図)
    intension_match = {}  # パターンマッチの結果を格納するリスト
    for intensions in intension.keys():  # 意図を取得
        intension_text = list(intension.get(intensions))  # その意図の単語を取得
        intension_type = set(intension_text) & set(targets)  # 意図の単語とターゲット情報で一致するものを抽出
        intension_count = len(list(intension_type))  # set型になっているのでリストに変換しマッチした数を格納
        if intension_count != 0:  # 意図との一致数が0でなければ
            intension_match.update({intensions:intension_count})  # 特定の意図にマッチした数をその意図名と共に格納
    print(intension_match)
    '''
    # db操作
    db = sqlite3.connect('./database/credibility_assessment.db')  # dbへ接続
    db.commit()  # 変更をデータベースに反映
    db.close()  # データベースとの接続解除'''
#mng(target_i)  # 確認用に実行