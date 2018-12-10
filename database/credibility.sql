drop table twitter_data;
create table twitter_data(
  id integer primary key,
  clock integer,
  data text
);
insert into twitter_data(clock, data) values(12, "example");
