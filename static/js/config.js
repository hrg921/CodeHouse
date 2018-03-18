var FLASK_SERVER_LOCATION = 'http://175.126.105.155:5000';
var SITE_URL = "http://175.126.105.155:5000";

function noData(object) {
  if(object.val() === undefined || object.val().trim() === "")
  {
    alert("입력되지 않은 값이 있습니다.");
    return true;
  }
  return false;
}

function sendJsonDataWithFunction(method, action, data, func){
  return $.ajax({
    "url": action,
    "data": data,
    "method": method,
    contentType: 'application/json; charset=utf-8',
    success: function(data) {
      func(data);
    }
  });
}

function isEmail(strValue) {
  var regExp = /[0-9a-zA-Z][_0-9a-zA-Z-]*@[_0-9a-zA-Z-]+(\.[_0-9a-zA-Z-]+){1,2}$/;
  if(strValue.length == 0) { return false; }
  if (!strValue.match(regExp)) { return false; }
  return true;
}
