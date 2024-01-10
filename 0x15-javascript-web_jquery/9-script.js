$(document).ready(function() {
  let helloUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.getJSON(helloUrl, function(data) {
    $('DIV#hello').text(data['hello']);
  });
});
