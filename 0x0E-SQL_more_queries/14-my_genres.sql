-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
SELECT
	tv_genres.name
FROM
	-- Join three tables
	tv_genres
	JOIN
	tv_shows
	JOIN
	tv_show_genres
	ON
		-- Condiction to join, only Dexter show
		tv_genres.id = tv_show_genres.genre_id
		AND
		tv_shows.id = tv_show_genres.show_id
		AND
		tv_shows.title = 'Dexter'
ORDER BY
	tv_genres.name
;

