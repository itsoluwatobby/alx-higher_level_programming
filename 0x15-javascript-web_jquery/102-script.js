$(document).ready(function() {
  $('INPUT#btn_translate').click(function() {
    let language = $('INPUT#language_code').val();
    let langApiUrl = `https://hellosalut.stefanbohacek.dev?lang=${language}`;
    $.getJSON(langApiUrl, function(data) {
      $('DIV#hello').text(data['hello']);
    });
    $('INPUT#language_code').val('');
  });
});
