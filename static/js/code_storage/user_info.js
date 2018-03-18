$(function() {
  $.ajax({
    'url': FLASK_SERVER_LOCATION + '/user/me',
    'method': 'POST',
    success: function(data) {
      info = JSON.parse(data);
      $('#header_user_name').html(info.name);
      $('#header_user_job').html(info.job);
    }
  });
});
