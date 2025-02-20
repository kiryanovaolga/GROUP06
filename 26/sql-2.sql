select * from zamestnanec

-- delete from zamestnanec where id = 1

-- insert = create = vkládá nové záznamy

insert into zamestnanec (jmeno) values ('Peťa Král')

-- update zamestnanec set vek = length(jmeno)

select substr(jmeno, 0, 3) from zamestnanec

-- nastavím username na první 2 znaky ze jména a id
-- update zamestnanec set username = substr(jmeno, 0, 3) || cast(id as varchar(30))


