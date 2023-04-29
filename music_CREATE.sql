--жанры
create table if not exists genre (
	id serial primary key,
	name_genre varchar(20) not null
);

--исполнители
create table if not exists executor (
	id serial primary key,
	name_executor varchar(40) not null
);

--Альбом
create table if not exists album (
	id serial primary key,
	name_album varchar(20) not null,
	date_album varchar(10) not null
);

--треки
create table if not exists track (
	id serial primary key,
	name_track varchar(40) not null,
	duration_track varchar(20) not null,
	album_id integer not null references album(id)
);

--сборники
create table if not exists collection (
	id serial primary key,
	name_collection varchar(20) not null,
	date_collection varchar(10) not null
);

--жанр-исполнитель(промежуточная таблица)
create table if not exists genre_executor(
	genre_id integer references genre(id),
	executor_id integer references executor(id),
	constraint pk_ge primary key (genre_id, executor_id)
);

--альбом-исполнитель(промежуточная таблица)
create table if not exists album_executor(
	album_id integer references album(id),
	executor_id integer references executor(id),
	constraint pk_ae primary key (album_id, executor_id)
);

--трек-сборник(промежуточная таблица)
create table if not exists track_collection(
	track_id integer references track(id),
	collection_id integer references collection(id),
	constraint pk_tc primary key (track_id, collection_id)
);

alter table album alter column date_album type integer using (date_album::integer);

alter table track alter column duration_track type integer using (duration_track::integer);

alter table collection alter column date_collection type integer using (date_collection::integer);