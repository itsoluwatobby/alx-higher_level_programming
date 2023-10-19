-- lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating

SELECT title, SUM(rate) AS rating
  FROM tv_shows AS tvs
       INNER JOIN tv_show_ratings AS tsr
       ON tvs.id = tsr.show_id
 GROUP BY title
 ORDER BY rating DESC;
