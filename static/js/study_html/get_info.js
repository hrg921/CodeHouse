$(function() {
  $.ajax({
    'url': FLASK_SERVER_LOCATION + '/user/me',
    'method': 'POST',
    success: function(data) {
      info = JSON.parse(data);
      $('.profile_username').html(info.name);
      $('.profile_userclass').html(info.job);
    }
  });

  $.ajax({
    "url": FLASK_SERVER_LOCATION + "/user/process/front",
    "method": "POST",
    success: function(data) {
      info = JSON.parse(data);
      classes = [info['HTML'], info['CSS'], info['JS']];
      class_title = ['HTML', 'CSS', 'JS'];
      class_number = [12, 9, 10];
      $('.profile_expgauge_gaugebar').css('width', parseInt(parseInt(classes[0]) / class_number[0] * 100) + "%");
    }
  });
});
