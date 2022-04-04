--  lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT tvs.title, tvsg.genre_id
FROM
	tv_shows tvs
	INNER JOIN
	tv_show_genres tvsg
ON
	tvs.id = tvsg.show_id
ORDER BY
	tvs.title, tvsg.genre_id;

