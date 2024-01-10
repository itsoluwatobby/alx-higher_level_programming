$(document).ready(function() {
  $('DIV#add_item').click(function() {
    let list = $('<li>', {
      text: 'Item'
    });
    $('ul.my_list').append(list);
  });
});
