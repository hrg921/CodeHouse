$(function() {
  $('#ok_button').click(function() {
    user_edit_password({
      password: '#password',
      password_rewrite: '#password_rewrite'
    });
  });
});

function user_edit_password(json) {
  var password = $(json.password);
  var password_rewrite = $(json.password_rewrite);

  if(noData(password)) { return; }
  if(noData(password_rewrite)) { return; }
  if(password.val() != password_rewrite.val()) { alert('비밀번호와 비밀번호확인이 같지 않습니다'); return; }

  var jsonData = JSON.stringify({
    password : password.val()
  });

  var result = sendJsonDataWithFunction("POST", FLASK_SERVER_LOCATION + "/user/edit", encodeURIComponent(jsonData), checkEdited);
}

function checkEdited(data) {
  if(data === "no session") {
    alert("로그인 되어있지 않습니다");
    location.href = SITE_URL;
  } else if(data === "True") {
    alert("비밀번호 변경 완료");
    location.href = SITE_URL;
  }
}
