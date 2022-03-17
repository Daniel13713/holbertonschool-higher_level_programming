--  lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- Results must be sorted in ascending order by the show title
SELECT
	DISTINCT -- unique elements, shows
	tv_shows.title
FROM
	-- first and extern join, we need join with left join becouse
	-- we must include all show that haven't gender Comedy, even those without any gener
	tv_shows
	LEFT JOIN
	(
		tv_genres,
		tv_show_genres
	)
	ON
	-- Condictions to general tables
	(
		tv_shows.id = tv_show_genres.show_id 
		AND
		tv_genres.id = tv_show_genres.genre_id
	)
WHERE
	tv_shows.title
	NOT IN
	(
		-- this is a list, all shows that have Comedy genere
		SELECT 
			tv_shows.title
		FROM
			tv_shows
			-- inner join
			JOIN
			(
				tv_genres,
				tv_show_genres
			)
			-- Condictions to select only show with Comedy genere
			ON
			(
				tv_shows.id = tv_show_genres.show_id 
				AND
				tv_genres.id = tv_show_genres.genre_id
				AND
				tv_genres.name = 'Comedy'
			)
		--  sort inner join
		ORDER BY
			tv_shows.title)
-- Sort outer join
ORDER BY
	tv_shows.title
;

