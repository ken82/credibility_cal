#!/usr/local/bin/python3
#_*_coding:utf-8_*_
# NLPによりMatrix Node Graphを生成する
import os, sys
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
    # ターゲット情報に対して意図分類を行いマトリクスを生成---------------------------------------------------------------------------
    # 上の行列と同じ構造を持つ意図分類マトリクスを生成
    target_intension = np.array([
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]])
 
    # NLPによりマトリクスへの分類-----------------------------------------------------------------------------------------------
    # 辞書とのパターンマッチング(もっともシンプルな方法を用いる)
    gazetteer_category = "./dict/category.json"  # カテゴリーに関するガゼッティア(固有表現辞書)
    category = json.load(open(gazetteer_category, encoding='utf-8'))  # カテゴリーのjsonを開く(日本語が含まれるのでエンコード)
    gazetteer_intension = "./dict/intension.json"  # 意図に関するガゼッティア
    intension = json.load(open(gazetteer_intension, encoding='utf-8'))  # 意図のjsonを開く
    pprint.pprint(intension)


    '''
    # db操作
    db = sqlite3.connect('./database/credibility_assessment.db')  # dbへ接続
    db.commit()  # 変更をデータベースに反映
    db.close()  # データベースとの接続解除'''
#mng(target_i)  # 確認用に実行