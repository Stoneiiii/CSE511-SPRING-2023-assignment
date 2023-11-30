# leihu3-assignment-1

#### 1.Thanks for grading my assignment.

#### 2.The following commands are not included into my .sql file, because it may have some impact on the grading environment.
postgres=#  set fsync='off';

postgres=#  set synchronous_commit='off';

postgres=#  set full_page_writes='off';

postgres=#  set bgwriter_lru_maxpages=0;

postgres=#  set wal_level='minimal';

postgres=#  set archive_mode='off';

postgres=#  set work_mem='64MB';

postgres=#  set max_wal_senders=0;

postgres=#  set maintenance_work_mem='64MB';

postgres=#  set shared_buffers='128MB';

#### 3.Note: my table names all have prefix: public

#### 4.My process
Create table -> import data -> set key and constraint
