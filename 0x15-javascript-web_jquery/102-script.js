$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const language = $('INPUT#language_code').val();
    const langApiUrl = `https://hellosalut.stefanbohacek.dev?lang=${language}`;
    $.getJSON(langApiUrl, function (data) {
      $('DIV#hello').text(data.hello);
    });
    $('INPUT#language_code').val('');
  });
});
