#!/usr/local/bin/python3
#_*_coding:utf-8_*_
# NLPによりMatrix Node Graphを生成する
import os, sys
import sqlite3
import numpy as np
import time, datetime
import preprocessing

''' Intension Matrix(意図を分類するための二次元配列) 
x軸=カテゴリ, y軸=意図
Intension = [
["               ", "Disaster(災害)", "Accident(事故)", "Terrorism(テロ)", "Medical(医療)", "Society(社会)", "Politics(政治)"],
["Anxiety(不安)   ",      0,                0,                0,                0,                0,                0],
["Disruption(分裂)",      0,                0,                0,                0,                0,                0],
["Publicity(宣伝) ",      0,                0,                0,                0,                0,                0],
["Desire(願望)    ",      0,                0,                0,                0,                0,                0],
["Praise(賞賛)    ",      0,                0,                0,                0,                0,                0],
["Delight(愉快)   ",      0,                0,                0,                0,                0,                0],
["Obligation(義務)",      0,                0,                0,                0,                0,                0],
["Politics(政治)  ",      0,                0,                0,                0,                0,                0],
]
Intension Matrixの実態は上の形の行列だが実際には 0 のセルだけを作成'''

target_i = input()  # 確認用
def mng(target_i)
    judge_result = (preprocessing.judge_lang(target_i))  # 言語判定モジュールを実行
    
    # db操作

    db = sqlite3.connect('./database/credibility_assessment.db')  # dbへ接続
    # データベースへの反映と接続解除
    db.commit()  # 変更をデータベースに保存
    db.close()  # データベースとの接続解除