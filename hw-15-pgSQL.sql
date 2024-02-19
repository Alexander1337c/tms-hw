# 1 задание
drop table if exists sales;
drop table if exists books;
drop table if exists authors;

CREATE TABLE authors(
	id SERIAL PRIMARY KEY,
	first_name text,
	last_name text
);

CREATE TABLE books(
	id SERIAL PRIMARY KEY,
	title text,
	author_id int REFERENCES authors(id),
	publication_year int
);

CREATE TABLE sales(
	id SERIAL PRIMARY KEY,
	book_id int REFERENCES books(id),
	quantity int
);

INSERT INTO authors(first_name, last_name)
values
('Алан','Болье'),
('Аллен','Тейлор'),
('Уолтер','Шилдс'),
('Энтони','Молинаро'),
('Барт','Монак');

INSERT INTO sales(book_id, quantity)
VALUES
(3, 15),
(1, 42),
(2, 31),
(4, 26),
(5, 7),
(6, 0),
(7, 15),
(8, 13),

INSERT INTO books (title, author_id, publication_year)
VALUES
('SQL. Сборник рецептов',4, 2003),
('Быстрое погружение. SQL',3, 1997),
('SQL для чайников',2, 1989),
('Изучаем SQL',1, 2000),
('Вы не знаете SQL'),
('SQL, Some Book',4, 2002),
('SQL Server',3, 1999),
('Oraqle SQL',2, 1988),
('SQL Dev',1, 2007);

# 2 Задание

select a.first_name,
	a.last_name,
	b.title
from authors as a
INNER JOIN books as b ON a.id = b.author_id

select a.first_name,
	a.last_name,
	b.title
from authors as a
LEFT JOIN books as b ON a.id = b.author_id

select
	b.title,
	a.first_name,
	a.last_name,
	b.publication_year
from authors as a
RIGHT JOIN books as b ON a.id = b.author_id;

# 3 Задание

select a.first_name, a.last_name, b.title, s.quantity
from authors AS a
INNER JOIN books as b ON a.id = b.author_id
INNER JOIN sales as s ON b.author_id = s.book_id

select a.first_name, a.last_name, b.title, s.quantity
from authors AS a
LEFT JOIN books as b ON a.id = b.author_id
LEFT JOIN sales as s ON b.author_id = s.book_id



# 4 Задание

select a.first_name, a.last_name, sum(s.quantity)
from authors as a
inner join books as b on b.author_id = a.id
inner join sales as s on s.book_id = b.id
group by a.first_name, a.last_name

select a.first_name, a.last_name, sum(s.quantity)
from authors as a
left join books as b on b.author_id = a.id
left join sales as s on s.book_id = b.id
group by a.first_name, a.last_name

# 5 Задание

select first_name, last_name,
	(select sum(s.quantity) from sales as s
	 join books as b on b.author_id = a.id
	 where s.book_id = b.id
	) as max_sale
from authors as a
order by max_sale desc
limit 1;


select a.first_name, a.last_name, b.title, s.quantity from authors as a
inner join books as b on b.author_id = a.id
inner join sales as s on s.book_id = b.id
where s.quantity > (select avg(s.quantity) from sales as s)

select a.first_name, a.last_name, avg(s.quantity) from authors as a
inner join books as b on b.author_id = a.id
inner join sales as s on s.book_id = b.id
group by a.first_name, a.last_name
having avg(s.quantity) > (
	select avg(sales.quantity) from sales
)