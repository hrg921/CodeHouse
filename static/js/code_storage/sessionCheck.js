$(function() {
  $.ajax({
    "url": FLASK_SERVER_LOCATION + "/user/isSession"
  });
});
