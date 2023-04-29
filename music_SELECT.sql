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



