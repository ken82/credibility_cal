--credibility_assessment.db操作のSQLファイル

--#################################################################################

--Twitter data 格納用テーブル
--drop table twitter_data;  -- テーブルのリセット
/*create table twitter_data(  -- テーブルの作成(ツイッターから取得したデータを入れるテーブル)
  id integer primary key,  -- id
  clock integer,  -- 取得した時間を格納
  data text  -- ツイートの本文を格納
);
-- サンプルのデータを一件格納
insert into twitter_data(clock, data) values(12, "example");*/

--#################################################################################

--Germanwings Crash 流言格納用テーブル
--drop table rumor_germanwings;  -- テーブルのリセット(すでに存在する場合は)
/*create table rumor_germanwings(
  id integer primary key,  -- id
  time integer,  -- タイムスタンプ
  data text  -- 本文
);
-- サンプルのデータを一件格納(sqliteはデータを格納しないとテーブルが消える)
insert into rumor_germanwings(time, data) values(12, "example");*/

--#################################################################################

--Ottawa Shooting 流言格納用テーブル
--drop table rumor_ottawashooting;  -- テーブルのリセット(すでに存在する場合は)
/*create table rumor_ottawashooting(
  id integer primary key,  -- id
  time integer,  -- タイムスタンプ
  data text  -- 本文
);
-- サンプルのデータを一件格納(sqliteはデータを格納しないとテーブルが消える)
insert into rumor_ottawashooting(time, data) values(12, "example");*/

--#################################################################################

--Sydney Siege 流言格納用テーブル
--drop table rumor_sydneysiege;  -- テーブルのリセット(すでに存在する場合は)
/*create table rumor_sydneysiege(
  id integer primary key,  -- id
  time integer,  -- タイムスタンプ
  data text  -- 本文
);
-- サンプルのデータを一件格納(sqliteはデータを格納しないとテーブルが消える)
insert into rumor_sydneysiege(time, data) values(12, "example");*/

--#################################################################################