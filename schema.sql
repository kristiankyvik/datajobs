DROP TABLE IF EXISTS job;
DROP TABLE IF EXISTS tag;
DROP TABLE IF EXISTS job_tag;

create table job (
  id integer primary key autoincrement,
  ref_number varchar(30) not null,
  title varchar(500) not null,
  company varchar(500) not null,
  location varchar(500) not null,
  description text not null,
  url varchar(500) not null,
  language varchar(500),
  tags varchar,
  published date not null
);

create table tag (
  id integer primary key autoincrement,
  title varchar(500) not null
);

create table job_tag (
  id integer primary key autoincrement,
  title varchar(500) not null
);
