$(document).ready(function () {
  const alxApiUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.getJSON(alxApiUrl, function (data) {
    const results = data.results.map(res => res.title);
    results.forEach(title => {
      const list = $('<li>', {
        text: title
      });
      $('UL#list_movies').append(list);
    });
  });
});
