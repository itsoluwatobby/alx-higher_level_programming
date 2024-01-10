$(document).ready(function () {
  $('DIV#add_item').click(function () {
    const list = $('<li>', {
      text: 'Item'
    });
    $('ul.my_list').append(list);
  });
});
