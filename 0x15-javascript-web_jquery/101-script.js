$(document).ready(function() {
  let lastItem = 0, id = 1;
  $('DIV#add_item').click(function() {
    let list = $('<li>', {
      id: 'list-' + id,
      text: 'Item'
    });
    lastItem = id;
    id++;
    $('ul.my_list').append(list);
  });

  $('DIV#remove_item').click(function() {
    let list = $('<li>', {
      text: 'Item'
    });
    $(`#list-${lastItem}`).remove();
    lastItem--;
  });

  $('DIV#clear_list').click(function() {
    $('li').remove();
    lastItem = 0, id = 1;
  });
});
