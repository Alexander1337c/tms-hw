create table Employees (
	Name Text,
	Position Text,
	Department Text,
	Salary INTEGER
);
INSERT INTO Employees (Name, Position, Department, Salary)
Values ('Alexander','front-end','dev',2000 ),
('Max','Driver','delivery',1500),
('Egor','account-manager','financial-dp',3200);
drop table Employees

UPDATE Employees
SET department='Sales'
WHERE name = 'Alexander';
alter table Employees
add column HireDate Text;
update Employees
set HireDate='12.08.2020' where name = 'Max';
update Employees
set HireDate='25.12.2017' where name = 'Alexander';
update Employees
set HireDate='06.10.2019' where name = 'Egor';
select * from Employees where position='Manager';
select * from Employees where salary > 5000;
select ROUND(avg(salary),0) as avg_salary from Employees;

select * from Employees
DROP TABLE Employees;