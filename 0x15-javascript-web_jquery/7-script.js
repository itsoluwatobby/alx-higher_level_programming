$(document).ready(function() {
  let alxApiUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.getJSON(alxApiUrl, function(data) {
    $('DIV#character').text(data['name']);
  });
});
