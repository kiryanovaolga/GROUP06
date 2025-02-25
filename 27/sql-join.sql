select * from tracks
inner join genres on genres.GenreId = tracks.GenreId
inner join media_types on media_types.MediaTypeId = tracks.MediaTypeId
where tracks.GenreId in (3,4)
limit 1000

-- vyber mi všechno z tracks
-- a k tomu připoj tabulku media_types, kde (on)
-- je shoda MediaTypeId v obou tabulkách
select * from tracks
inner join media_types on media_types.MediaTypeId = tracks.MediaTypeId

select * from albums
inner join artists on artists.ArtistId = albums.ArtistId
limit 10

select name from genres
where name like 'R%'
