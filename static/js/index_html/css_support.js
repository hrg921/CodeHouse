$(function() {
  $('.maker_image_container').css('width', $('.maker_image_container').css('height'));
  $(window).resize(function() {
    $('.maker_image_container').css('width', $('.maker_image_container').css('height'));
  });
});
// $( window ).resize(function() {
//   $( "#log" ).append( "<div>Handler for .resize() called.</div>" );
// });
