-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
SELECT
	tv_genres.name, -- obtain name of the generes
	SUM(tv_show_ratings.rate) AS rating -- sum only rate colunm
FROM
	-- join all tables
	tv_genres
	JOIN
	(
		tv_show_genres,
		tv_show_ratings,
		tv_shows
	)
	-- condictions to join all tables
	ON
	(
		tv_genres.id = tv_show_genres.genre_id
		AND
		tv_shows.id = tv_show_genres.show_id
		AND
		tv_shows.id = tv_show_ratings.show_id
		AND
		tv_show_genres.show_id = tv_show_ratings.show_id
	)
-- rows where sum will execute
GROUP BY
	tv_genres.name
-- Sort by rating value descending
ORDER BY
	rating
	DESC
;

