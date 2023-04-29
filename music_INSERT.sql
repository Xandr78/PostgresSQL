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
values ('альбом 1', 2000),
	('альбом 2', 1997),
	('альбом 3', 2015),
	('альбом 4', 2000),
	('альбом 5', 2011)
;

UPDATE album 
SET name_album = 'альбом 4', date_album = 2018
WHERE id = 13;

UPDATE track 
SET name_track = 'trackmy1', duration_track = 6, album_id = 10
WHERE id = 1;

insert  into track (name_track, duration_track, album_id)
values ('track_1', 3, 10),
	('track_2', 2, 10),
	('track_3', 3, 11),
	('track_4', 6, 11),
	('track_5', 5, 11),
	('track_6', 2, 12),
	('track_7', 3, 12),
	('track_8', 4, 12),
	('track_9', 3.5, 12),
	('track_10', 5, 13),
	('track_11', 3, 13),
	('track_12', 2, 13),
	('track_13', 4, 13),
	('track_14', 1, 13),
	('track_15', 3, 14)
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
values (3, 4),
	(3, 5),
	(3, 7),
	(4, 9),
	(4, 11),
	(7, 10),
	(6, 6),
	(5, 8),
	(5, 10),
	(3, 11),
	(6, 11)
;

insert into album_executor (album_id, executor_id)
values (10, 4),
	(10, 10),
	(10, 11),
	(11, 4),
	(11, 5),
	(11, 6),
	(12, 4),
	(12, 7),
	(12, 11),
	(13, 4),
	(13, 7),
	(13, 10),
	(14, 8),
	(14, 9),
	(14, 11)

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

    