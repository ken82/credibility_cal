--credibility.dbに実験用テーブルを格納するためのSQL
/*
drop table rumor_germanwings_all;  -- テーブルのリセット

-- テーブルの作成(germanwings墜落事故のrumor格納用)
create table rumor_germanwings_all(
  id integer primary key,  -- id
  time integer,  -- タイムスタンプ
  data text,  -- 本文
  source_id integer  -- 同じsourceの識別ID
);

-- サンプルのデータを一件格納
insert into rumor_germanwings_all(time, data, source_id) values(12, "example", 1);
*/
