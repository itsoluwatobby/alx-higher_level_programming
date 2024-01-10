$(document).ready(function() {
  $('INPUT#btn_translate').click(function() {
    let language = $('INPUT#language_code').val();
    let langApiUrl = `https://hellosalut.stefanbohacek.dev?lang=${language}`;
    $.getJSON(langApiUrl, function(data) {
      $('DIV#hello').text(data['hello']);
    });
    $('INPUT#language_code').val('');
  });
 
  $('INPUT#language_code').focus(function() {
    $('INPUT#language_code').keyup(function(event) {
      if (event.key === 'Enter') {
        let language = $('INPUT#language_code').val();
        let langApiUrl = `https://hellosalut.stefanbohacek.dev?lang=${language}`;
        $.getJSON(langApiUrl, function(data) {
          $('DIV#hello').text(data['hello']);
        });
        $('INPUT#language_code').val('');
      }
    });
  });
});
