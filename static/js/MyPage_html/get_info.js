$(function() {
  $.ajax({
    "url": FLASK_SERVER_LOCATION + "/user/me",
    "method": "POST",
    success: function(data) {
      info = JSON.parse(data);
      $('#process_count').html(info.course_ing);
      $('#complete_count').html(info.course_ed);
      $('#skill_count').html(info.skillcount);
    }
  });

  $.ajax({
    "url": FLASK_SERVER_LOCATION + "/user/process",
    "method": "POST",
    success: function(data) {
      info = JSON.parse(data);
      $('#front-end').css('height', info['front-end'] + "%");
      $('#server').css('height', info.server + "%");
      $('#c-developer').css('height', info['C-DEV'] + "%");
      $('#db-manager').css('height', info['DB-MNG'] + "%");
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
      count = 0;
      for(i = 0; i < 3; i++) {
        if(classes[i] > 0 && classes[i] < 100) {
          $('#ing_contents_container').append('<div class="ing_contents"><h1 class="ing_contents_title">' + class_title[i] + '</h1>' + '<span class="vertical_align_middle"></span><div class="ing_contents_graph_bar"><div class="ing_contents_graph" id="' + class_title[i] + '"></div></div><p class="ing_contents_percent">' + parseInt(parseInt(classes[i]) / class_number[i] * 100) + '%</p></div>');
          count++;
          $('#' + class_title[i]).css('width', parseInt(parseInt(classes[i]) / class_number[i] * 100) + "%");
          $('#process_graph_' + class_title[i].toLowerCase()).css('width', parseInt(parseInt(classes[i]) / class_number[i] * 100) + "%");
        }
      }
      if(count == 0) {
        $('#ing_contents_container').html('<p id="no_processing">현재 진행중인 코스가 없습니다.</p>');
      }
    }
  })
});

// <div class="ing_contents">
//   <h1 class="ing_contents_title">HTML</h1>
//   <span class="vertical_align_middle"></span>
//   <div class="ing_contents_graph_bar">
//     <div class="ing_contents_graph" id="HTML"></div>
//   </div>
//   <p class="ing_contents_percent">50%</p>
// </div>
