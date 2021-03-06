#!/usr/local/bin/python3
#_*_coding:utf-8_*_
# 信憑性計測システム．フォームからの入力を受け取り前処理(英語か日本語かを判定)を行う
# このプログラムでは前処理と，その結果に応じた信憑性計測関数の実行，CGIの出力のみを行う
import sys, io, os
import cgi, cgitb
import preprocessing
import co_occurrence_tw
import co_occurrence_db
import db_operation
import mng

# cgi設定------------------------------------------------------------------------
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')  # pythonのcgiで日本語が文字化けするのを防ぐ
cgitb.enable()  # エラーがあった場合に出力させる
print("Content-Type: text/html")  # HTML is following
print()  # blank line, end of headers
# formの受け取り-----------------------------------------------------------------
form = cgi.FieldStorage()
input = form.getvalue("target")  # Target Information
target = str(input)  # fromで受け取った値が NoneType 型になっているので変換．この"target"変数が大元のtarget informationとなる
# html上部-----------------------------------------------------------------------
html_head = """
<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<title>Credibility Assessment</title>
<link rel="stylesheet" href="./style.css">
</head>
<body>
<header>
<div id="header">
<a href="./index.html">Credibility Assessment System</a></div>
</header><br><br><br><br>
<h2>Result</h2><hr>
"""
print(html_head)  # htmlの上部の出力

# pythonによるデータ処理---------------------------------------------------------
print("Target Information : \"" + target + "\"")  # 入力されたデータをブラウザに表示
print("<br>")
print("Language : ")
excution_flag = 0  # 前処理を行なった結果信憑性評価を行うかどうかの判定に使うフラグ

# 入力データが英語か日本語かを判定する(自然言語処理を行うので，英語か日本語かによって方式が変わる)
judge_result = (preprocessing.judge_lang(target))  # 言語判定を実行
print(judge_result)  # 結果をprint
print("<br>")
print("Key Word : ")

# 英語版の処理-------------------------------------------------------------------
if judge_result == "English":
    target = target.lower()  # 英語は全て小文字に変換
    context_en_result = preprocessing.context_en(target)  # 形態素解析で英語のテキストを簡易的に文脈判断
    if context_en_result == 0:  # 0は伝聞推定ではない．
        #target_i = preprocessing.morpho_en(target)  # 形態素解析で英語文章の名詞・動詞(キーワード)を抽出
        target_i = target  # 上の関数を実行しない
        print(target_i)  # 表示
        if target_i != "None":  # 値が無効でなければ
            excution_flag = 1  # 前処理の結果，英語の信憑性評価を実行
    else:  # 伝聞推定なので，キーワードだけ表示し信憑性評価は行わない
        print(target)
else:
    pass

# 日本語版の処理-----------------------------------------------------------------
if judge_result == "Japanese":
    context_ja_result = preprocessing.context_ja(target)  # 文脈判断の関数を実行し，結果を格納(断定形なら0, 伝聞・推定形なら1)
    if context_ja_result == 0:  # 0は伝聞推定ではない．
        target_i = preprocessing.morpho_ja(target)  # 関数の実行結果(キーワード)を格納
        print(target_i)  # 表示．
        if target_i != "Error":  # 値が無効でなければ
            excution_flag = 2  # 前処理の結果，日本語の信憑性評価を実行
    else:  # 伝聞推定なので，キーワードだけ表示して信憑性評価は行わない
        print(preprocessing.morpho_ja(target))
else:
    pass
print("<br><hr>")
# 受け取ったデータの前処理はここまで

# Matrix Node Graphに関する関数の実行----------------------------------------------
# 現在は英語の前処理でフラグが立っても日本語の前処理でフラグがたってもこの関数を実行する仕様になっている
if excution_flag == 1 or excution_flag == 2:
    print("We will excute credibility assessment.<br><hr>")
    print(co_occurrence_tw.cotw(target_i))  # 共起情報の収集関数を実行(ここではTwitterのみ)
    # print(co_occurrence_db.codb(target_i))  # DBから共起情報を取得する(実験用)
    
    #  Intension Matrixを生成
    intension_matrixes = {}  # ターゲット情報とその類似情報全てのマトリクスを格納すすためのdict
    target_matrix, category, intension = mng.mngMatrix(target_i)
    #intension_matrixes.setdefault("timestamp", target_matrix)  # マトリクス格納用dictに追加

    # 取得したマトリクスを表示
    print("The Intension Matrix<br>")
    for result in target_matrix:
        print(result)
        print("<br>")
    # カテゴリ表示
    print("Category -> ")
    print(category)
    # 意図も表示
    print("<br>Intension -> ")
    print(intension)
    print("<br><hr><br>")

    # 類似情報のマトリクスを取得
    print("The similar information of the target information.<br><br>")
    sim = []  # 類似情報を格納するためのリスト
    similar_information = db_operation.search("rumor_germanwings","muslim")  # db操作の関数を実行しdb内に格納されたデータを取得(テーブル名, キーワード)現在は決め打ち
    #similar_information = db_operation.search("rumor_ottawashooting","suspects")
    #similar_information = db_operation.search("rumor_sydneysiege","held hostage")

    for sim_info in similar_information:  # sqlite3のcursorオブジェクトとして入ってきたデータを一つずつ取り出し
        sim.append(sim_info)  # タプルとして追加
    sim = list(sim)  # リストに変換
    for simdata in sim:  # データ一つずつ取り出す
        print(simdata[2])  # 取り出したデータは二次元になっており[0]はid，[1]がタイムスタンプ，[2]が本文
        print("<br><br>")
        print(simdata[1])  # タイムスタンプも表示する
        print("<br>")
        # 本文の意図マトリクスを生成
        simdata_matrix, simdata_category, simdata_intension = mng.mngMatrix(simdata[2])
        intension_matrixes.setdefault(simdata[1], simdata_matrix)  # 取得したマトリクスをタイムスタンプと共にはまとめていく
        for simmatrix in simdata_matrix:  # 配列のままだと見づらいので1つずつ
            print(simmatrix)  # 表示
            print("<br>")
        print("Category -> ")
        print(simdata_category)
        print("<br>Intension -> ")
        print(simdata_intension)
        print("<br>")
        print("<hr>")

    # Matrix Node Graphの生成
    # matrixNodeGraph = mng.mngGraph(intension_matrixes)  # dictにまとめたタイムスタンプとマトリクスを渡す
    # print(matrixNodeGraph)

else:  # フラグが立っていないので何もしない
    print("※ Error：We cannot assess the credibility of this information. Because The value is invalid or the credibility of this information is low.<br>")

# html下部----------------------------------------------------------------------
print("<br><hr>")
html_bottom = """
<div id="back">
<a href="./index.html">Back</a>
</body></html>
"""
print(html_bottom)  # htmlのラストを出力して完了
