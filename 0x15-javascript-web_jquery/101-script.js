$(document).ready(function () {
  let lastItem = 0;
  let id = 1;
  $('DIV#add_item').click(function () {
    const list = $('<li>', {
      id: 'list-' + id,
      text: 'Item'
    });
    lastItem = id;
    id++;
    $('ul.my_list').append(list);
  });

  $('DIV#remove_item').click(function () {
    $(`#list-${lastItem}`).remove();
    lastItem--;
  });

  $('DIV#clear_list').click(function () {
    $('li').remove();
    lastItem = 0;
    id = 1;
  });
});
