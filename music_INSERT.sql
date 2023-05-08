 insert  into genre(name_genre)
values ('Рок'),
	('Поп'),
	('Соул'),
	('Шансон'),
	('Рэп')
;

insert  into executor (name_executor)
values ('Linkin Park'),
	('Король и Шут'),
	('Владимир Высоцкий'),
	('Limp bizkit'),
	('Любэ'),
	('Земфира'),
	('Макс Корж'),
	('Трофим')
;

insert into album (name_album, date_album)
values ('альбом 1', 2019),
	('альбом 2', 1997),
	('альбом 3', 2020),
	('альбом 4', 2018),
	('альбом 5', 2011)
;

--UPDATE album 
--SET name_album = 'альбом 4', date_album = 2018
--WHERE id = 13;

--UPDATE album 
--SET name_album = 'альбом 1', date_album = 2019
--WHERE id = 10;

--update album
--set name_album = 'альбом 3', date_album =2020
--where id = 12;

--UPDATE track 
--   name_track = 'trackmy1', duration_track = 6, album_id = 10
--WHERE id = 1;

--update album_executor
--set album_id = 13, executor_id = 8
--where album_id = 13 and executor_id = 7

insert  into track (name_track, duration_track, album_id)
values ('track_new', 3, 5);

insert  into track (name_track, duration_track, album_id)
values ('trackmy1', 6, 1),
	('track_2', 2, 1),
	('track_3', 3, 2),
	('track_4', 6, 2),
	('track_5', 5, 2),
	('track_6', 2, 3),
	('track_7', 3, 3),
	('track_8', 4, 3),
	('track_9', 3.5, 3),
	('track_10', 5, 4),
	('track_11', 3, 4),
	('track_12', 2, 4),
	('track_13', 4, 4),
	('track_14', 1, 4),
	('trackмой15', 3, 5)
;

insert into collection (name_collection, date_collection)
values ('сборник 1', 2001),
	('сборник 2', 2016),
	('сборник 3', 2012),
	('сборник 4', 1999),
	('сборник 5', 2013),
	('сборник 6', 2002),
	('сборник 7', 2003),
	('сборник 8', 2020)
;

insert into genre_executor (genre_id, executor_id)
values (1, 1),
	(1, 2),
	(1, 4),
	(2, 6),
	(2, 8),
	(5, 7),
	(4, 3),
	(3, 5),
	(3, 7),
	(1, 8),
	(4, 8)
;

insert into album_executor (album_id, executor_id)
values (1, 1),
	(1, 7),
	(1, 8),
	(2, 1),
	(2, 2),
	(2, 3),
	(3, 1),
	(3, 4),
	(3, 8),
	(4, 1),
	(4, 5),
	(4, 7),
	(5, 5),
	(5, 6),
	(5, 8)

;

insert into track_collection (track_id, collection_id)
values (1, 1),
	(1, 2),
	(2, 1),
	(2, 3),
	(3, 1),
	(3, 4),
	(4, 1),
	(4, 5),
	(5, 2),
	(5, 6),
	(6, 2),
	(6, 7),
	(7, 2),
	(7, 8),
	(8, 1),
	(9, 2),
	(10, 3),
	(11, 4),
	(12, 5),
	(13, 6),
	(14, 7),
	(15, 8)
;

--update  genre
--set name_genre = 'хип-хоп'
--where id = 2

--delete from genre  
--where id < 13 and id > 7

    