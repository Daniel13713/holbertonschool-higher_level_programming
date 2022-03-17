-- ulist all genres not linked to the show Dexter
SELECT
	DISTINCT -- Unique element
	tv_genres.name -- First selection of generes
FROM
	-- First join of all tables
	tv_genres
	JOIN
	tv_shows
	JOIN
	tv_show_genres
	ON
		-- Fisrt Condiction to join all tables
		tv_genres.id = tv_show_genres.genre_id
		AND
		tv_shows.id = tv_show_genres.show_id
WHERE
	tv_genres.name -- condition to choose only generes that haven't Dexter show
	NOT IN
		(SELECT
			-- Second selection of generes
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
			-- order second Join
			tv_genres.name)
ORDER BY
	-- Order First and extern table joined
	tv_genres.name
;

