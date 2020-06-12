makeRequest();
    function updateRequestUrl(url) {
        document.getElementById('request-url-input').value = url;
        makeRequest();
    }
    function makeRequest() {
        var url = document.getElementById('request-url-input').value;
        var request = new XMLHttpRequest();
        request.onreadystatechange = function() {
            if (request.readyState == XMLHttpRequest.DONE) 
            {
                if (request.status == 200) 
                {
                    var jsonData = JSON.parse(request.responseText);
                    document.getElementById('response-output').innerHTML = JSON.stringify(jsonData, null, '\t');
                } 
                else if (request.status == 404) 
                {
                    document.getElementById('response-output').innerHTML =
                        'Could not find any resource that matches the request, try again!';
                } 
                else 
                {
                    document.getElementById('response-output').innerHTML =
                        'Somethin went wrong. Try again, or contact tjlite81@gmail.com';
                }
            }
        };
        request.open('GET', url);
        request.send();
    }