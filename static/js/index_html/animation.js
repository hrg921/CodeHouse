var selected = ['#sign_in_select_box', '#signIn_box'];
var nonselected = ['#sign_up_select_box', '#signUp_box'];

$(function() {
  $('.login_menu').click(function() {
    if($(this).hasClass('nonselected'))
      switch_box();
  });
});

function switch_box() {
  $(selected[0]).removeClass('selected').addClass('nonselected');
  $(selected[1]).css('display', 'none');
  $(nonselected[0]).removeClass('nonselected').addClass('selected');
  $(nonselected[1]).css('display', 'block');
  var temp0 = selected[0];
  var temp1 = selected[1];
  selected[0] = nonselected[0];
  selected[1] = nonselected[1];
  nonselected[0] = temp0;
  nonselected[1] = temp1;
}
