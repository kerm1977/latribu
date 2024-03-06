function myFunction() {
var x = document.getElementById("pass");
  var i = document.getElementById("pass1");
  var o = document.getElementById("pass2");
 
  icon = document.querySelector("i.icon");
  if(i.type === "password" && o.type === "password" || x.type === "password") {
    x.type = "text";
    i.type = "text";
    o.type = "text";
    icon.classList.remove("icon-eye")
    icon.classList.add("icon-eye-blocked")
  }else {
  	x.type = "password";
    i.type = "password";
    o.type = "password";
    icon.classList.add("icon-eye")
  	icon.classList.remove("icon-eye-blocked")
  }
}

