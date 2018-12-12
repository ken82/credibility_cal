--credibility.dbに収集データを格納するためのSQL
drop table rumor_germanwings;  -- テーブルのリセット

-- テーブルの作成(germanwings墜落事故のrumor格納用)
create table rumor_germanwings(
  id integer primary key,  -- id
  time integer,  -- タイムスタンプ
  data text  -- 本文
);

-- サンプルのデータを一件格納
insert into rumor_germanwings(time, data) values(12, "example");