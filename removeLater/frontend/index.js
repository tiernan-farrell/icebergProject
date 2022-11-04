var xhr = null;
getXmlHttpRequestObject = function () {
    if (!xhr) {
        // Create a new XMLHttpRequest object 
        xhr = new XMLHttpRequest();
    }
    return xhr;
};
function dataCallback() {
    // Check response is ready or not
    if (xhr.readyState == 4 && xhr.status == 200) {
        console.log("User data received!");
        getDate();
        dataDiv = document.getElementById('result-container');
        // Set current data text
        dataDiv.innerHTML = xhr.responseText;
    }
}
function getData() {
    console.log("Get data...");
    xhr = getXmlHttpRequestObject();
    xhr.onreadystatechange = dataCallback;
    // asynchronous requests
    xhr.open("GET", "http://localhost:6969/data", true);
    // Ssend the request over the network
    xhr.send(null);
}
async function getBucResults() { 
    console.log("Get Buc...");
    xhr = getXmlHttpRequestObject(); 
    xhr.onreadystatechange = dataCallback; 
    await xhr.open("GET", "http://localhost:6969/buc", true)
    xhr.send(null)
}
async function getAprioriResults() { 
    console.log("Get Apriori...");
    xhr = getXmlHttpRequestObject(); 
    xhr.onreadystatechange = dataCallback; 
    await xhr.open("GET", "http://localhost:6969/apriori", true)
    xhr.send(null)
}
async function getTdcResults() { 
    console.log("Get Top Down Computation...");
    xhr = getXmlHttpRequestObject(); 
    xhr.onreadystatechange = dataCallback; 
    await xhr.open("GET", "http://localhost:6969/tdc", true)
    xhr.send(null)
}
async function getStarCubeResults() { 
    console.log("Get star Cube...");
    xhr = getXmlHttpRequestObject(); 
    xhr.onreadystatechange = dataCallback; 
    await xhr.open("GET", "http://localhost:6969/starCube", true)
    xhr.send(null)
}
async function getTimes() { 
    console.log("Getting times...");
    xhr = getXmlHttpRequestObject(); 
    xhr.onreadystatechange = dataCallback; 
    await xhr.open("GET", "http://localhost:6969/getComputationTimes", true)
    xhr.send(null)
}
function getDate() {
    date = new Date().toString();
    document.getElementById('time-container').textContent
        = date;
}
(function () {
    getDate();
})();