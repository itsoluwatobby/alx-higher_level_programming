-- A script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name

SELECT DISTINCT name FROM tv_genres AS tg
       INNER JOIN tv_show_genres AS tsg
       ON tg.id = tsg.genre_id

       INNER JOIN tv_shows AS tvs
       ON tsg.show_id = tvs.id
       WHERE tg.name NOT IN
             (SELECT name FROM tv_genres AS tg
	             INNER JOIN tv_show_genres AS tsg
		     ON tg.id = tsg.genre_id

		     INNER JOIN tv_shows AS tvs
		     ON tsg.show_id = tvs.id
		     WHERE tvs.title = "Dexter")
 ORDER BY tg.name;
