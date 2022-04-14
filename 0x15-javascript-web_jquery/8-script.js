$(() => {
  const URL = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.get(URL, (data, status) => {
    data.results.forEach((movie) => {
      $('UL#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
