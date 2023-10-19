-- lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by the rating

SELECT tg.name, SUM(rate) AS rating
 FROM tv_genres AS tg
	INNER JOIN tv_show_genres AS tsg
       	ON tsg.genre_id = tg.id

       	INNER JOIN tv_show_ratings AS tsr
       	ON tsr.show_id = tsg.show_id
 GROUP BY tg.name
 ORDER BY rating DESC;
