function logout() {
  $.ajax({
    'url': '/user/logout',
    'method': 'POST',
    success: function(data) {
        location.href = "/"
    }
  });
}

// function sendJsonDataWithFunction(method, action, data, func){
  // return $.ajax({
  //   "url": action,
  //   "data": data,
  //   "method": method,
  //   contentType: 'application/json; charset=utf-8',
  //   success: function(data) {
  //     func(data);
  //   }
  // });
