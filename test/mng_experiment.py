#!/usr/local/bin/python3
#_*_coding:utf-8_*_
# mng実験用スクリプト(手動で動かす時に使う)
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# MNGが生成できるかどうかの実験
# 実験1 (入力: BREAKING German Media Site Says Germanwings Co-Pilot Was Muslim Convert)-----------------
g = nx.DiGraph()  # 空の有向グラフを生成
# 1段目--------------------------------
# ひとつ目のグラフは無条件でノードになる
g.add_node("Fri Mar 27 01:19:22 2015")  # Agitation': 2, 'Publicity': 1, 'Fun': 1, 'Obligation': 1
# TimeWindow = 3時間で
# もし一つ前の上のノードと 意図が違ければ追加 同じものなら無視
g.add_node("Fri Mar 27 01:59:52 2015")  # Agitation': 1
g.add_node("Fri Mar 27 02:53:05 2015")  # Agitation': 2, 'Desire': 1
# 2段目--------------------------------
g.add_node("Fri Mar 27 10:37:14 2015")  # Agitation': 1, 'Admire': 1, 'Politics': 1
g.add_node("Fri Mar 27 10:40:10 2015")  # Agitation': 1
# 3段目--------------------------------
g.add_node("Fri Mar 27 15:32:55 2015")  # Anxiety': 2
# 4段目--------------------------------
g.add_node("Fri Mar 27 20:02:23 2015")  # 'Agitation': 2, 'Publicity': 1, 'Fun': 1, 'Obligation': 1
g.add_node("Fri Mar 27 20:17:38 2015")  # Agitation': 1
# エッジの接続(1段目->2段目)
g.add_edge("Fri Mar 27 01:19:22 2015","Fri Mar 27 10:37:14 2015")
g.add_edge("Fri Mar 27 01:19:22 2015","Fri Mar 27 10:40:10 2015")
g.add_edge("Fri Mar 27 01:59:52 2015","Fri Mar 27 10:37:14 2015")
g.add_edge("Fri Mar 27 01:59:52 2015","Fri Mar 27 10:40:10 2015")
g.add_edge("Fri Mar 27 02:53:05 2015","Fri Mar 27 10:37:14 2015")
g.add_edge("Fri Mar 27 02:53:05 2015","Fri Mar 27 10:40:10 2015")
# エッジの接続(2段目->3段目)
g.add_edge("Fri Mar 27 10:37:14 2015","Fri Mar 27 15:32:55 2015")
g.add_edge("Fri Mar 27 10:40:10 2015","Fri Mar 27 15:32:55 2015")
# エッジの接続(3段目->4段目)
g.add_edge("Fri Mar 27 15:32:55 2015","Fri Mar 27 20:02:23 2015")
g.add_edge("Fri Mar 27 15:32:55 2015","Fri Mar 27 20:17:38 2015")
# nx.draw(g)  # 描画
# plt.show()  # 表示


# 実験2(入力: )--------------------------------------------------------------
g2 = nx.DiGraph()  # 空の有向グラフを生成
# 1段目--------------------------------
# ひとつ目のグラフは無条件でノードになる
g2.add_node("Wed Oct 22 15:15:14 2014")  # Anxiety': 1, 'Publicity': 1, 'Desire': 1, 'Obligation': 1
# TimeWindow = 3時間で
# もし一つ前の上のノードと 意図が違ければ追加 同じものなら無視
g2.add_node("Wed Oct 22 15:25:07 2014")  # Politics': 1}
g2.add_node("Wed Oct 22 15:29:36 2014")  # 'Anxiety': 2, 'Publicity': 1, 'Politics': 1
g2.add_node("Wed Oct 22 15:41:38 2014")  # Anxiety': 1, 'Publicity': 1
# 2段目--------------------------------
g2.add_node("Wed Oct 22 18:33:04 2014")  # Anxiety': 1, 'Publicity': 1
g2.add_node("Wed Oct 22 16:19:05 2014")  # Anxiety': 1, 'Publicity': 1
g2.add_node("Wed Oct 22 15:19:14 2014")  # Anxiety': 1, 'Publicity': 1, 'Desire': 1, 'Obligation': 1
# エッジの接続(1段目->2段目)
g2.add_edge("Wed Oct 22 15:15:14 2014","Wed Oct 22 18:33:04 2014")
g2.add_edge("Wed Oct 22 15:15:14 2014","Wed Oct 22 16:19:05 2014")
g2.add_edge("Wed Oct 22 15:15:14 2014","Wed Oct 22 15:19:14 2014")
g2.add_edge("Wed Oct 22 15:25:07 2014","Wed Oct 22 18:33:04 2014")
g2.add_edge("Wed Oct 22 15:25:07 2014","Wed Oct 22 16:19:05 2014")
g2.add_edge("Wed Oct 22 15:25:07 2014","Wed Oct 22 15:19:14 2014")
g2.add_edge("Wed Oct 22 15:29:36 2014","Wed Oct 22 18:33:04 2014")
g2.add_edge("Wed Oct 22 15:29:36 2014","Wed Oct 22 16:19:05 2014")
g2.add_edge("Wed Oct 22 15:29:36 2014","Wed Oct 22 15:19:14 2014")
g2.add_edge("Wed Oct 22 15:41:38 2014","Wed Oct 22 18:33:04 2014")
g2.add_edge("Wed Oct 22 15:41:38 2014","Wed Oct 22 16:19:05 2014")
g2.add_edge("Wed Oct 22 15:41:38 2014","Wed Oct 22 15:19:14 2014")
# nx.draw(g2)  # 描画
# plt.show()  # 表示

# 実験3(入力: )--------------------------------------------------------------
g3 = nx.DiGraph()  # 空の有向グラフを生成
# 1段目--------------------------------
# ひとつ目のグラフは無条件でノードになる
g3.add_node("Sun Dec 14 23:26:03 2014")  # 'Anxiety': 1, 'Publicity': 1
# TimeWindow = 3時間で
# もし一つ前の上のノードと 意図が違ければ追加 同じものなら無視
g3.add_node("Mon Dec 15 01:07:38 2014")  # 'Anxiety': 2, 'Publicity': 1, 'Obligation': 1
# 2段目--------------------------------
g3.add_node("Mon Dec 15 04:00:28 2014")  # Anxiety': 1, 'Publicity': 1, 'Obligation': 1
# エッジの接続(1段目->2段目)
g3.add_edge("Sun Dec 14 23:26:03 2014","Mon Dec 15 04:00:28 2014")
g3.add_edge("Mon Dec 15 01:07:38 2014","Mon Dec 15 04:00:28 2014")
# nx.draw(g3)  # 描画
# plt.show()  # 表示




# マトリクス間の距離を測る--------------------------------------------
# mng1-------------------------------
mng1_1 = np.array([
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0.5, 0, 0, 0.25, 0, 0.25, 0], 
[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0]])
mng1_2 = np.array([
[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 1, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0]])
mng1_3 = np.array([
[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0.666, 0, 0, 0.333, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0]])
# mng1下段
mng1_4 = np.array([
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0.4, 0.2, 0.2, 0, 0, 0.2, 0], 
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]])
mng1_5 = np.array([
[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]])
# mng2-------------------------------
mng2_1 = np.array([
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0.25, 0, 0.25, 0, 0.25, 0, 0.25, 0], 
[0, 0, 0, 0, 0, 0, 0, 0]])
mng2_2 = np.array([
[0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1]])
mng2_3 = np.array([
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0.25, 0, 0.125, 0, 0, 0, 0, 0.125], 
[0.25, 0, 0.125, 0, 0, 0, 0, 0.125]])
mng2_4 = np.array([
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0.5, 0, 0.5, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0]])
# mng2下段
mng2_5 = np.array([
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0.25, 0, 0.25, 0, 0, 0, 0, 0],
[0.25, 0, 0.25, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]])
mng2_6 = np.array([
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0.5, 0, 0.5, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0]])
mng2_7 = np.array([
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0.25, 0, 0.25, 0, 0.25, 0, 0.25, 0, ],
[0, 0, 0, 0, 0, 0, 0, 0]])
# mng3-------------------------------
mng3_1 = np.array([
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0.25, 0, 0.25, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0], 
[0.25, 0, 0.25, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0]])
mng3_2 = np.array([
[0.166, 0, 0.083, 0, 0, 0, 0.083, 0], 
[0, 0, 0, 0, 0, 0, 0, 0,],
[0.166, 0, 0.083, 0, 0, 0, 0.083, 0], 
[0, 0, 0, 0, 0, 0, 0, 0,],
[0.166, 0, 0.083, 0, 0, 0, 0.083, 0], 
[0, 0, 0, 0, 0, 0, 0, 0]])
# mng3下段
mng3_3 = np.array([
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0.166, 0, 0.166, 0, 0, 0, 0.166, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0.166, 0, 0.166, 0, 0, 0, 0.166, 0],
[0, 0, 0, 0, 0, 0, 0, 0]])



# マトリクス間の類似度
def matrixDistance(m1, m2):
    mat_dist = []  # マトリクス間の距離計算用リスト
    sub = m1 - m2  # 二つのマトリクスの差を求め
    distance = list(map(lambda x: x**2, sub))  # その差を2乗
    for dist in distance:  # 各行を取り出し
        for d in dist:  # 各要素を抜き出し
            mat_dist.append(d)  # 一つにまとめる
    Dm = sum(mat_dist)  # 総和を求めて距離を計算
    return Dm



# 実験1 mng1とmng2の類似度-------------------------------------------------------
mng1_mng2_head = []  # 上段の距離
mng1_mng2_head.append(matrixDistance(mng1_1, mng2_1))  # mng1_1とmng2-1の距離
mng1_mng2_head.append(matrixDistance(mng1_1, mng2_2))
mng1_mng2_head.append(matrixDistance(mng1_1, mng2_3))
mng1_mng2_head.append(matrixDistance(mng1_1, mng2_4))
mng1_mng2_head.append(matrixDistance(mng1_2, mng2_1))
mng1_mng2_head.append(matrixDistance(mng1_2, mng2_2))
mng1_mng2_head.append(matrixDistance(mng1_2, mng2_3))
mng1_mng2_head.append(matrixDistance(mng1_2, mng2_4))
mng1_mng2_head.append(matrixDistance(mng1_3, mng2_1))
mng1_mng2_head.append(matrixDistance(mng1_3, mng2_2))
mng1_mng2_head.append(matrixDistance(mng1_3, mng2_3))
mng1_mng2_head.append(matrixDistance(mng1_3, mng2_4))
dist＿mng1_mng2_head = sum(mng1_mng2_head)  # mng1とmng2の上段の距離の合計
# 下段
mng1_mng2_bottom = []  # 下段の距離
mng1_mng2_bottom.append(matrixDistance(mng1_4, mng2_5))
mng1_mng2_bottom.append(matrixDistance(mng1_4, mng2_6))
mng1_mng2_bottom.append(matrixDistance(mng1_4, mng2_7))
mng1_mng2_bottom.append(matrixDistance(mng1_5, mng2_5))
mng1_mng2_bottom.append(matrixDistance(mng1_5, mng2_6))
mng1_mng2_bottom.append(matrixDistance(mng1_5, mng2_7))
dist＿mng1_mng2_bottom = sum(mng1_mng2_bottom)  # mng1とmng2の下段の距離の合計
print("mng1とmng2の距離")
d_m1m2 = (dist＿mng1_mng2_head/12)+(dist＿mng1_mng2_bottom/6)  # 上段下段それぞれ総当たりの回数で割って平均を取り，さらに上下の平均を取る
print(d_m1m2/2)
distance1 = nx.graph_edit_distance(g,g2)  # グラフgとグラフg2の距離
print("mng1とmng2のグラフの距離")
print(distance1)
print("\n\n\n")



# 実験2 mng1とmng3の類似度---------------------------------------------------------
mng1_mng3_head = []  # 上段の距離
mng1_mng3_head.append(matrixDistance(mng1_1, mng3_1))  # mng1_1とmng3-1の距離
mng1_mng3_head.append(matrixDistance(mng1_1, mng3_2))
mng1_mng3_head.append(matrixDistance(mng1_2, mng3_1))
mng1_mng3_head.append(matrixDistance(mng1_2, mng3_2))
mng1_mng3_head.append(matrixDistance(mng1_3, mng3_1))
mng1_mng3_head.append(matrixDistance(mng1_3, mng3_2))
dist＿mng1_mng3_head = sum(mng1_mng3_head)  # mng1とmng2の上段の距離の合計
# 下段
mng1_mng3_bottom = []  # 下段の距離
mng1_mng3_bottom.append(matrixDistance(mng1_4, mng3_3))
mng1_mng3_bottom.append(matrixDistance(mng1_5, mng3_3))
dist＿mng1_mng3_bottom = sum(mng1_mng3_bottom)  # mng1とmng2の下段の距離の合計
print("mng1とmng3の距離")
d_m1m3 = (dist＿mng1_mng3_head/6) + (dist＿mng1_mng3_bottom/2)
print(d_m1m3/2)
# mng１とmng2のグラフの距離
distance2 = nx.graph_edit_distance(g,g3)  # グラフgとグラフg2の距離
print("mng1とmng3のグラフの距離")
print(distance2)
print("\n\n\n")


# 実験3 mng2とmng3の類似度-------------------------------------------------------
mng2_mng3_head = []  # 上段の距離
mng2_mng3_head.append(matrixDistance(mng2_1, mng3_1))  # mng1_1とmng2-1の距離
mng2_mng3_head.append(matrixDistance(mng2_1, mng3_2))
mng2_mng3_head.append(matrixDistance(mng2_2, mng3_1))
mng2_mng3_head.append(matrixDistance(mng2_2, mng3_2))
mng2_mng3_head.append(matrixDistance(mng2_3, mng3_1))
mng2_mng3_head.append(matrixDistance(mng2_3, mng3_2))
mng2_mng3_head.append(matrixDistance(mng2_4, mng3_1))
mng2_mng3_head.append(matrixDistance(mng2_4, mng3_2))
dist＿mng2_mng3_head = sum(mng2_mng3_head)  # mng1とmng2の上段の距離の合計
# 下段
mng2_mng3_bottom = []  # 下段の距離
mng2_mng3_bottom.append(matrixDistance(mng2_5, mng3_3))
mng2_mng3_bottom.append(matrixDistance(mng2_6, mng3_3))
mng2_mng3_bottom.append(matrixDistance(mng2_7, mng3_3))
dist＿mng2_mng3_bottom = sum(mng2_mng3_bottom)  # mng1とmng2の下段の距離の合計
print("mng2とmng3の距離")
d_m2m3 = (dist＿mng2_mng3_head/8) + (dist＿mng2_mng3_bottom/3)
print(d_m2m3/2)
distance3 = nx.graph_edit_distance(g2,g3)  # グラフgとグラフg2の距離
print("mng2とmng3のグラフの距離")
print(distance3)