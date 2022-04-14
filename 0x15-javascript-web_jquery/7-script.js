$(() => {
  const URL = 'https://swapi-api.hbtn.io/api/people/1/?format=json';
  $.get(URL, (data, status) => {
    $('DIV#character').text(data.name);
  });
});
