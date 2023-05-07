--Название и год выхода альбомов, вышедших в 2018 году.
select  name_album, date_album from album
where date_album = 2018

--Название и продолжительность самого длительного трека.
select name_track  as "самый длительный трек", duration_track from track
where  duration_track = (select max(duration_track) from track)

--Название треков, продолжительность которых не менее 3,5 минут.
select name_track, duration_track from track
where duration_track  >= 3.5

--Названия сборников, вышедших в период с 2018 по 2020 год включительно.
select name_collection from collection
where date_collection between 2018 and 2020

--Исполнители, чьё имя состоит из одного слова.
select name_executor from executor
where name_executor not like '% %'

--Название треков, которые содержат слово «мой» или «my».
select name_track from track
where name_track like '%my%' or name_track like '%мой%'


--Домашнее задание к лекции «Продвинутая выборка данных»
--Количество исполнителей в каждом жанре.
select name_genre, count(ge.executor_id) from genre as g
join genre_executor as ge on g.id = ge.genre_id 
group by g.name_genre 

--Количество треков, вошедших в альбомы 2019–2020 годов.
select count(t.id) from album a 
join track t on t.album_id = a.id 
where a.date_album  between 2019 and 2020;

--select a.name_album, count(t.id) from album a 
--join track t on t.album_id = a.id 
--where a.date_album  between 2019 and 2020
--group by a.name_album;

--Средняя продолжительность треков по каждому альбому.
select a.name_album, avg(t.duration_track) from album a
join track t on a.id = t.album_id 
group by a.name_album;

--Все исполнители, которые не выпустили альбомы в 2020 году.
select name_executor from executor e
where e.name_executor not in (select name_executor  from executor e 
								join album_executor ae on ae.executor_id = e.id 
								join album a on a.id = ae.album_id 
								where a.date_album = 2020);

--select name_executor  from executor e 
--join album_executor ae on ae.executor_id = e.id 
--join album a on a.id = ae.album_id 
--where a.date_album <> 2020
--group by e.name_executor;

--Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами).
select name_collection, name_executor as "исполнитель из сборника" from collection c 
join track_collection tc on c.id = tc.collection_id 
join track t on t.id = tc.track_id 
join album a on a.id = t.album_id 
join album_executor ae on ae.album_id = a.id 
join executor e on e.id = ae.executor_id 
where e.name_executor = 'Земфира'

--Названия альбомов, в которых присутствуют исполнители более чем одного жанра.
select name_album, e.name_executor  from album a 
join album_executor ae on ae.album_id = a.id 
join executor e on e.id = ae.executor_id 
join genre_executor ge on ge.executor_id = e.id 
join genre g on g.id = ge.genre_id 
group by a.name_album, e.name_executor  
having count(ge.genre_id) > 1

--Наименования треков, которые не входят в сборники.
select name_track as "не в сборниках" from track t 
left join track_collection tc on tc.track_id = t.id 
where tc.track_id  isnull

--Исполнитель или исполнители, написавшие самый короткий по продолжительности трек, — теоретически таких треков может быть несколько.
select name_executor from executor e 
join album_executor ae on ae.executor_id = e.id 
join album a on a.id = ae.album_id 
join track t on t.album_id = a.id 
where t.duration_track = (select min(t.duration_track) from track t)

--Названия альбомов, содержащих наименьшее количество треков.
SELECT name_album, COUNT(t.id) FROM album a 
JOIN track t ON t.album_id = a.id
GROUP BY a.id
HAVING COUNT(t.id) = (SELECT COUNT(t.id) FROM track t
    						GROUP BY t.album_id 
    						ORDER BY count(t.id) 
    						LIMIT 1
    						);