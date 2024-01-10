$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const language = $('INPUT#language_code').val();
    const langApiUrl = `https://hellosalut.stefanbohacek.dev?lang=${language}`;
    $.getJSON(langApiUrl, function (data) {
      $('DIV#hello').text(data.hello);
    });
    $('INPUT#language_code').val('');
  });

  $('INPUT#language_code').focus(function () {
    $('INPUT#language_code').keyup(function (event) {
      if (event.key === 'Enter') {
        const language = $('INPUT#language_code').val();
        const langApiUrl = `https://hellosalut.stefanbohacek.dev?lang=${language}`;
        $.getJSON(langApiUrl, function (data) {
          $('DIV#hello').text(data.hello);
        });
        $('INPUT#language_code').val('');
      }
    });
  });
});
