-- сотрудники
create table if not exists employee (
	id serial primary key,
	name_employee varchar(20) not null
);

-- начальники (связь 1 ко 1)
create table if not exists chief (
	post_chief varchar(20) not null,
	employee_id integer primary key references employee(id)
);

-- изменение в таблице "сотрудники" (добавляем колонку "департамент")
--alter table employee add column department varchar(20) not null;
