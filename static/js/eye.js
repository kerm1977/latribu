function myFunction1() {
  var x = document.getElementById("password");
 
  icon = document.querySelector("i.icon");
  if(x.type === "password") {
    x.type = "text";
    icon.classList.remove("icon-eye")
    icon.classList.add("icon-eye-blocked")
  }else {
    x.type = "password";

    icon.classList.add("icon-eye")
    icon.classList.remove("icon-eye-blocked")
  }
}



function myFunction() {
  var i = document.getElementById("password1");
  var o = document.getElementById("password2");
 
  icon = document.querySelector("i.icon");
  if(i.type === "password" && o.type === "password") {
    i.type = "text";
    o.type = "text";
    icon.classList.remove("icon-eye")
    icon.classList.add("icon-eye-blocked")
  }else {
    i.type = "password";
    o.type = "password";
    icon.classList.add("icon-eye")
    icon.classList.remove("icon-eye-blocked")
  }
}