$(function() {

  $('#signup_button').click(function() {
    user_register({
      email: "#email_input_box2",
      name: "#name_input_box2",
      password: "#pw_input_box2"
    });
  });

  $('#login_button').click(function() {
    user_login({
      email : "#email_input_box1",
      password : "#pw_input_box1"
    });
  });
});

// json = [email, name, password]
function user_register(json) {
  var email = $(json.email);
  var username = $(json.name);
  var password = $(json.password);

  if(noData(email)) { return; }
  if(noData(username)) { return; }
  if(noData(password)) { return; }

  if(!isEmail(email.val())) {
    alert("입력하신 이메일의 형식이 올바르지 않습니다.");
    return;
  }

  var jsonData = JSON.stringify({
    email : email.val(),
    name : username.val(),
    password : password.val()
  });

  var result = sendJsonDataWithFunction("POST", FLASK_SERVER_LOCATION + "/user/register", encodeURIComponent(jsonData), checkRegistered);

}

var checkRegistered = function(data) {
  if(data === "False") {
    alert("이 이메일은 사용중입니다.");
    return;
  }

  console.log(data);

  alert("회원가입이 완료되었습니다.");
  location.href = SITE_URL;
}

// json = [email, password]
function user_login(json) {
  var email = $(json.email);
  var password = $(json.password);

  if(noData(email)) { return; }
  if(noData(password)) { return; }

  if(!isEmail(email.val())) {
    alert("입력하신 이메일의 형식이 올바르지 않습니다.");
    return;
  }

  var jsonData = JSON.stringify({
    email : email.val(),
    password : password.val()
  });

  var result = sendJsonDataWithFunction("POST", FLASK_SERVER_LOCATION + "/user/login", encodeURIComponent(jsonData), isCorrectUser);

}

var isCorrectUser = function(data) {
  if(data === "False") {
    alert("아이디 또는 비밀번호가 잘못되었습니다.");
    return;
  }
  location.href = SITE_URL + "/myPage";
}
