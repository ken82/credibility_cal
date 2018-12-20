#!/usr/local/bin/python3
#_*_coding:utf-8_*_
# NLPによりMatrix Node Graphを生成する
import os, sys
import json
import codecs
import pandas
import sklearn
import sqlite3
import numpy as np
import time, datetime
import preprocessing
# Intension Matrix(意図を分類するための二次元配列) 
'''x軸=カテゴリ, y軸=意図
Intension = [
["               ", "Disaster(災害)", "Accident(事故)", "Terrorism(テロ)", "Medical(医療)", "Society(社会)", "Politics(政治)"],
["Anxiety(不安)   ",      0,                0,                0,                0,                0,                0],
["Disruption(分裂)",      0,                0,                0,                0,                0,                0],
["Publicity(宣伝) ",      0,                0,                0,                0,                0,                0],
["Desire(願望)    ",      0,                0,                0,                0,                0,                0],
["Praise(賞賛)    ",      0,                0,                0,                0,                0,                0],
["Delight(愉快)   ",      0,                0,                0,                0,                0,                0],
["Obligation(義務)",      0,                0,                0,                0,                0,                0],
["Politics(政治)  ",      0,                0,                0,                0,                0,                0]
]
Intension Matrixの実態は上の形の行列だが実際には 0 のセルだけを作成'''
#target_i = input()  # 確認用
def mng(target_i):
    judge_result = (preprocessing.judge_lang(target_i))  # 言語判定モジュールを実行
    # ターゲット情報に対して意図分類を行いマトリクスを生成---------------------------------------------------------------------------
    # 上の行列と同じ構造を持つ意図分類マトリクスを生成
    target_intension = np.array([
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
    ])
 
    # NLPによりマトリクスへの分類-----------------------------------------------------------------------------------------------
    # 辞書とのパターンマッチング
    gazetteer_category = "./dict/category.json"  # カテゴリーに関するガゼッティア(固有表現辞書)
    category = json.load(open(gazetteer_category))  # カテゴリーのjsonを開く
    print(category)
    gazetteer_intension = "./dict/intension.json"  # 意図に関するガゼッティア
    intension = json.load(open(gazetteer_intension))  # 意図のjsonを開く
    print(intension)


    '''
    # db操作
    db = sqlite3.connect('./database/credibility_assessment.db')  # dbへ接続
    db.commit()  # 変更をデータベースに反映
    db.close()  # データベースとの接続解除'''
#mng(target_i)  # 確認用に実行