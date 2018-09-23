
function log(text, level = "Info", txtAreaID) {
    var txtArea = document.getElementById("console")

    if (txtArea.value == "") {
        txtArea.value = "[" + level + "] : " + text + '\n'
    } else {
        txtArea.value += "[" + level + "] : " + text + '\n'
    }
}

function get_video_chunk(url) {
    return new Promise(function (resolve, reject) {
        var httpRequest = new XMLHttpRequest();
        httpRequest.open("GET", url);
        httpRequest.responseType = "arraybuffer";

        httpRequest.onload = function () {
            resolve(httpRequest.response);
        };

        httpRequest.onerror = reject;
        httpRequest.send();
    });
}

function get_metadata(base, id) {
    var url = base + "?id=" + id

    return new Promise(function (resolve, reject) {
        var httpRequest = new XMLHttpRequest();
        httpRequest.open("GET", url);
        httpRequest.responseType = "json";

        httpRequest.onload = function () {
            resolve(httpRequest.response);
        };

        httpRequest.onerror = reject;
        httpRequest.send();
    });
}

function url_create(base, id, segment, quality = null) {
    if (quality == null) {
        return base + "?" + "id=" + id + "&segment=" + segment
    }else{
        return base + "?" + "id=" + id + "&segment=" + segment + "&quality=" + quality
    }
}
