-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL
SELECT 
	tvs.title,
	tvsg.genre_id
FROM
	tv_shows tvs -- acronym for column
	LEFT JOIN
	tv_show_genres tvsg -- acronym for column
ON
	tvs.id = tvsg.show_id -- Condiction
WHERE
	tvsg.show_id IS NULL
ORDER BY
	tvs.title, tvsg.genre_id;

