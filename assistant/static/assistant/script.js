function sendCommand() {
    let command = document.getElementById("command").value;
    fetch(`/get/?command=${command}`)
        .then(res => res.json())
        .then(data => {
            document.getElementById("response").innerText = data.response;
        });
}

function voiceCommand() {
    fetch(`/get/?command=voice`)
        .then(res => res.json())
        .then(data => {
            document.getElementById("response").innerText = data.response;
        });
}
