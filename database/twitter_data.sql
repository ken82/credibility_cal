--credibility.dbに収集データを格納するためのSQL
drop table twitter_data;  -- テーブルのリセット

-- テーブルの作成(ツイッターから取得したデータを入れるテーブル)
create table twitter_data(
  id integer primary key,  -- id
  clock integer,  -- 取得した時間を格納
  data text  -- ツイートの本文を格納
);

-- サンプルのデータを一件格納
insert into twitter_data(clock, data) values(12, "example");
