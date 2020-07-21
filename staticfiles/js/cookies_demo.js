const output = document.querySelector('.output');
const btns = document.querySelectorAll('button');
const getVals = document.querySelectorAll('input');

function btnAction(e) {
   let temp = e.srcElement.innerText.substr(0,e.srcElement.innerText.indexOf(" "))
   let v = {};
   getVals.forEach( (item,index) => {
      let tempName = item.getAttribute('name');
      let tempValue = tempName != "cookieExpire" ? item.value: item.valueAsDate;
      v[tempName] = tempValue;
   })
   console.log(v);

   if(temp == 'Set') {
      setCookie(v.cookieName, v.cookieValue, v.cookieExpire);
   } else if (temp == 'Get') {
      getCookie(v.cookieName);
   } else if (temp == 'Delete') {
      eraseCookie(v.cookieName);
   } else if (temp == 'All') {
      listCookies();
   }
}

function setCookie(name, value, exp) {
   if(value.length > 0){
      document.cookie = name + "=" + encodeURIComponent(value) + "; path=/; expires=" + exp.toUTCString();
      output.textContent = "Cookie " + name + " has been set!";
   } else {
      output.textContent = "Cookie needs a value";
   }
}

function getCookie(name) {
   let cookies = document.cookie.split(";");
   output.textContent = "No Cookies Found";
   cookies.forEach( (item,index) => {
      item = item.trim();
      let tempCookie = item.split("=");
      if(tempCookie[0] === name) {
         output.textContent = "Found cookie: " + tempCookie[0].trim() + " is " + decodeURIComponent(tempCookie[1]);
      }
   })
}

function eraseCookie(name) {
   document.cookie = name + "; path=/; expires=Thu, 01 Jan 1970 00:00:01 GMT;" + exp.toUTCString();
   output.textContent = "Cookie " + name + " Removed";
}

function listCookies() {
   let cookies = document.cookie.split(";");
   output.textContent = "";
   cookies.forEach(function (item, index) {
      item = item.trim();
      let tempCookie = item.split("=");
      if (tempCookie[0].length > 0) {
         let div = document.createElement("div");
         div.setAttribute("class", "cookie");
         div.addEventListener("click", function () {
            eraseCookie(tempCookie[0]);
         })
         div.textContent = tempCookie[0].trim() + " " + decodeURIComponent(tempCookie[1]);
         output.appendChild(div);
      }
   })
}

btns.forEach( btn => {
   btn.addEventListener('click', btnAction);
})

document.addEventListener('DOMContentLoaded', () =>{
   const now = new Date();
   let nextWeek = (now.getDate() + 7);
   console.log(nextWeek);
   let day = ("0"+nextWeek).slice(-2);
   let month = ("0"+(now.getMonth()+1)).slice(-2);
   let year = now.getFullYear();
   document.querySelector('input[type=date]').value = year + '-' + month + '-' + day;
})
