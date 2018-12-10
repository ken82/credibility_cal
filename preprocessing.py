#!/usr/local/bin/python3
#_*_coding:utf-8_*_
# NLPの前処理を行う関数群
import re
import nltk
import MeCab
import unicodedata
from bs4 import BeautifulSoup
from polyglot.text import Text
from nltk.corpus import wordnet
from collections import namedtuple
from janome.tokenizer import Tokenizer

# 入力されたテキストが英語か日本語か判定する
def judge_lang(target):
    for ch in target:
        word = unicodedata.name(ch)
        if "CJK UNIFIED" in word or "HIRAGANA" in word or "KATAKANA" in word:
            return("Japanese")  # 漢字・ひらがな・カタカナが含まれたら日本語
    return("English")  # 含まれなければ英語

# 正規表現によるテキストのクリーニング
def clean_text(text):
    replaced_text = '\n'.join(s.strip() for s in text.splitlines()[2:] if s != '')  # skip header by [2:]
    replaced_text = replaced_text.lower()
    replaced_text = re.sub(r'[【】]', ' ', replaced_text)  # 【】の除去
    replaced_text = re.sub(r'[（）()]', ' ', replaced_text)  # （）の除去
    replaced_text = re.sub(r'[［］\[\]]', ' ', replaced_text)  # ［］の除去
    replaced_text = re.sub(r'[@＠]\w+', '', replaced_text)  # メンションの除去
    replaced_text = re.sub(r'https?:\/\/.*?[\r\n ]', '', replaced_text)  # URLの除去
    replaced_text = re.sub(r'　', ' ', replaced_text)  # 全角空白の除去
    replaced_text = re.sub(r'\n', ' ', replaced_text)  # 改行の除去
    return replaced_text
    
# 正規表現によるテキストのクリーニング(カスタム用)
def cleansing(raw_data):
    replaced_text = raw_data
    replaced_text = re.sub(r'\n', ' ', replaced_text)  # 改行の除去
    replaced_text = re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)", '', replaced_text)  # URLの除去
    return replaced_text


# URLを取り除く
def clean_url(html_text):
    clean_text = re.sub(r'http\S+', '', html_text)
    return clean_text

# テキストの正規化
def normalize(text):
    normalized_text = normalize_unicode(text)
    normalized_text = normalize_number(normalized_text)
    normalized_text = lower_text(normalized_text)
    return normalized_text

# Unicodeの正規化
def normalize_unicode(text, form='NFKC'):
    normalized_text = unicodedata.normalize(form, text)
    return normalized_text

# 数字の正規化
def normalize_number(text):
    # 連続した数字を0で置換
    replaced_text = re.sub(r'\d+', '0', text)
    return replaced_text

# 形態素解析で英語のテキストを簡易的に文脈判断
def context_en(target):
    tokens = Text(target)  # polyglotで単語を取得
    aux = []  # 助動詞を抽出
    for token in tokens.pos_tags:
        if token[1] == "AUX":  # 助動詞を取り出す
            aux.append(token[0])  # リストに格納
        else:
            aux.append("NONE")
    will, may, should = "will", "may", "should"  # 推定・意見の助動詞をパターンマッチング
    if will in aux or may in aux or should in aux:
        return(1)  # 含まれれば1
    else:
        return(0)  # 含まれなければ0

# 形態素解析で日本語のテキストを簡易的に文脈判断
def context_ja(target):
    global preprocessing_result  # 結果によって値を変えるフラグ
    t = None  # targetの解析結果を入れるグローバル変数を定義しておく
# Filtering by Regular Expression (正規表現で伝聞形，推量形は除く)
    pattern = re.compile(r'だろう|らしい|かもしれない|と思われる|だそうだ|とのこと')  # 伝聞・推定の形を手動で決めている
    match = pattern.findall(target)
    if match:
        return(1)  # 伝聞・推定形の場合1を返す
    else:
        return(0)  # 伝聞・推定形でなければ0を返す

# 形態素解析で英語文章の名詞・動詞を抽出(ストップワードの削除)
def morpho_en(target):
    tokens = Text(target)  # polyglotで単語を取得
    words_en = []  # 単語を入れる配列
    for token in tokens.pos_tags:
        if token[1] == "NOUN":  # 単語が名詞だったら取り出す
            words_en.append(token[0])  # リストに格納
        elif token[1] == "VERB":  # 動詞も取る
            words_en.append(token[0])  # リストに格納
    key_word = ', '.join(words_en)  # リストを一つにまとめる
    return(key_word)

# 形態素解析で日本語文章の名詞・動詞を抽出(ストップワードの削除)
def morpho_ja(target):
    tagger = MeCab.Tagger()  # MeCabのインスタンス
    tagger.parse('')  # 一度空の文字列をparseしないとエラー
    text_node = tagger.parseToNode(target)  # 解析
    words_ja = []  # 単語を格納するリスト．ここにtextの名詞が格納される
    while text_node:
        word = text_node.surface.split(",")[0]  # surfaceは単語を取得
        pos = text_node.feature.split(",")[0]  # featureは品詞(PartsOfSpeech)を取得
        if pos == "名詞" or pos == "動詞":  # 文章に名詞か動詞が含まれたら
            words_ja.append(word)  # その単語を取り出していく
        text_node = text_node.next  # nextで全形態素に順次アクセス
    if not words_ja:
        words_ja.append("Error")
    result = " ".join(words_ja)  # 抜き出したキーワードを文字列に変換し，空白で繋げて格納
    return result

# 参考URL
# https://qiita.com/Hironsan/items/2466fe0f344115aff177
