makeRequest();
    function updateRequestUrl(url) {
        document.getElementById('url-input').value = url; //update search box url with example when clicked
        makeRequest();
    }
    function makeRequest() {
        var url = document.getElementById('url-input').value;
        var request = new XMLHttpRequest();
        request.onreadystatechange = function() {
            if (request.readyState == XMLHttpRequest.DONE) 
            {
                if (request.status == 200) 
                {
                    var jsonData = JSON.parse(request.responseText);  //request.responseText returns the server response as a string of text (JSON in this case)
                    document.getElementById('url-output').innerHTML = JSON.stringify(jsonData, null, '\t'); 
                } 
                else if (request.status == 404) 
                {
                    document.getElementById('url-output').innerHTML =
                        'Could not find any resource that matches the request. Try again!';
                } 
                else 
                {
                    document.getElementById('url-output').innerHTML =
                        'Somethin went wrong. Try again, or contact tjlite81@gmail.com';
                }
            }
        };
        request.open('GET', url);
        request.send();
    }

var input = document.getElementById("url-input");
input.addEventListener("keyup", function(event) {
   if (event.keyCode === 13) 
   {
        event.preventDefault();
        document.getElementById("my-btn").click();
   }
});