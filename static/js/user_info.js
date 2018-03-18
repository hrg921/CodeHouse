$(function() {
  $.ajax({
    'url': FLASK_SERVER_LOCATION + '/user/me',
    'method': 'POST',
    success: function(data) {
      info = JSON.parse(data);
      $('#nav_profile_desc > h1').html(info.name);
      $('#nav_profile_desc > p').html(info.job);
    }
  });
});
