--insert into student (jmeno, prijmeni)
select DISTINCT jmeno_studenta, prijmeni_studenta from student_kurz_1

select * from student
select * from kurz
select * from student_kurz
-- delete from student_kurz
select * from student_kurz_1

insert into student_kurz values (100, 100)

--insert into kurz (nazev, cena)
select DISTINCT nazev_kurzu, cena_kurzu from student_kurz_1

--insert into student_kurz (student_id, kurz_id)
select DISTINCT student.id, kurz.id from student_kurz_1
inner join student on student.jmeno = student_kurz_1.jmeno_studenta
inner join kurz on kurz.nazev = student_kurz_1.nazev_kurzu


select s.jmeno, s.prijmeni, k.nazev, k.cena from student_kurz as sk
inner join student as s on s.id = sk.student_id
inner join kurz as k on k.id = sk.kurz_id


-- toto mi vrátí počet a celkou cenu pro jednotivé studenty
select s.jmeno, s.prijmeni, count(*), sum(k.cena) from student_kurz as sk
inner join student as s on s.id = sk.student_id
inner join kurz as k on k.id = sk.kurz_id
group by s.jmeno, s.prijmeni


select k.nazev, count(*), sum(k.cena) from student_kurz as sk
inner join student as s on s.id = sk.student_id
inner join kurz as k on k.id = sk.kurz_id
group by k.nazev
order by count(*) desc, k.nazev