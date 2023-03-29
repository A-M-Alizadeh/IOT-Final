const currentLocation = location.href;
const menuItem = document.querySelectorAll('a')
const menuLength = menuItem.length
for (let i = 0; i < menuLength; i++) {
  if (menuItem[i].href === currentLocation) {
    menuItem[i].className = "active"
  }
}

$(document).ready(function(){
  alert('Whattttt');
});

function loadDoc(){
  console.log("loadDoc");
}
