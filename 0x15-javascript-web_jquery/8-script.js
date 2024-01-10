$(document).ready(function() {
  let alxApiUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.getJSON(alxApiUrl, function(data) {
    let results = data.results.map(res => res.title);
    results.map(title => {
       let list = $('<li>', {
         text: title
       });
       $('UL#list_movies').append(list);
    });
  });
});
