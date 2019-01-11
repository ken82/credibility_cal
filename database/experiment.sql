--credibility.dbに収集データを格納するためのSQL
/*
drop table experiment_table;  -- テーブルのリセット

-- テーブルの作成(germanwings墜落事故のrumor格納用)
create table experiment_table(
  id integer primary key,  -- id
  time integer,  -- タイムスタンプ
  data text  -- 本文
);

-- サンプルのデータを一件格納
insert into experiment_table(time, data) values(12, "example");
*/