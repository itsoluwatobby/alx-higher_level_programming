-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title

SELECT DISTINCT title FROM tv_shows AS tvs
       LEFT JOIN tv_show_genres AS tsg
       ON tsg.show_id = tvs.id

       LEFT JOIN tv_genres AS tg
       ON tg.id = tsg.id
       WHERE tvs.title NOT IN
             (SELECT title FROM tv_shows AS tvs
	             INNER JOIN tv_show_genres AS tsg
		     ON tsg.show_id = tvs.id

		     INNER JOIN tv_genres AS tg
		     ON tg.id = tsg.genre_id
		     WHERE tg.name = "Comedy")
 ORDER BY tvs.title;
