-- sql

-- vyber vše z tabulky zamestnanec
SELECT * FROM zamestnanec limit 100

-- vyber mi všechny záznamy zamestnanec, kde id je větší než 2 nebo id je rovno 1
-- seřadit podle id sestuplně (od největšího, po nejmenší)
SELECT id, jmeno FROM zamestnanec
WHERE id > 2 or id = 1
ORDER BY id DESC -- ACS
LIMIT 40

-- vyber všechny zamestnanec, kde mají n ve jménu
select * from zamestnanec
where jmeno like '%n%'

-- úkol:
-- vyberte zamestnanece kteří mají id > 2 a zároveň mají písmeno 'a' kdekoliv
select * from zamestnanec
where id > 2 and jmeno like '%a%'

-- vybere počet řádků v tabulce
select count(*) from zamestnanec
-- další agregační funkce
select min(id) from zamestnanec
select max(id) from zamestnanec
select sum(id) from zamestnanec
select count(*), min(id), max(id), sum(id) from zamestnanec

select count(*), min(id), max(id), sum(id) from zamestnanec
where id > 2


---------------------------------------------------------------------
-- CRUD
-- C = create (SQL: INSERT)
-- R = retreive (SQL: SELECT)
-- U = update (SQL: UPDATE)
-- D = delete (SQL: DELETE)


-- UPDATE zamestnanec SET jmeno = 'Petr Novotný'

select * from zamestnanec where id = 2;
-- UPDATE zamestnanec set jmeno = 'Petr Novotný' where id = 2


-- UPDATE zamestnanec set jmeno =  '...hello'

-- změňte jmena na 'xyz' pro lidi, kteří mají ve svém jménu písmeno 'a'

-- toto vyisuje pokud udělá změnu: Query success. 5 rows affected

-- update zamestnanec set jmeno = 'xyz' where jmeno like '%h%'

delete from zamestnanec where id = 1


