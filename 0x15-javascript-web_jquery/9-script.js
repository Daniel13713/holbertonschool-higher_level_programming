$(() => {
  const URL = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.get(URL, (data, status) => {
    $('DIV#hello').append(data.hello);
  });
});
