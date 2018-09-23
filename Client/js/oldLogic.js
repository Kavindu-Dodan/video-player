/*
* Logic of video player
*/

function get_video_chunk(url){
    return new Promise(function(resolve, reject){
        var httpRequest = new XMLHttpRequest();
        httpRequest.open("GET", url);
        httpRequest.responseType = "blob";

        httpRequest.onload = function() {
          resolve(httpRequest.response);
        };

        httpRequest.onerror = reject;
        httpRequest.send();
    });
}

function get_meta(){
    return new Promise(function(resolve, reject){
        $.ajax({
            url: "http://localhost:9090/server/",
            type: "GET",
            dataType: "JSON",
            success: function(result){
                resolve(JSON.stringify(result))
            },
            error: function(error){
                reject(error)
            }
            }
        );
    });
}

function start_loop(){
    var video = document.getElementById("player");
    video.controls = false

    var source = document.createElement('source');
    source.setAttribute('type','video/mp4');

    var id = 0;

    get_video_chunk("http://localhost:9090/server/video?id="+ video_list[id])
    .then(function(blob){
        source.setAttribute('src', window.URL.createObjectURL(blob));
        video.appendChild(source);
        video.play();

        video.onended = function(){
            id ++;

            if (id >= video_list.length){
                id = 0;
            }

            get_video_chunk("http://localhost:9090/server/video?id=" + video_list[id])
            .then(function(blob){
                source.setAttribute('src', window.URL.createObjectURL(blob));
                video.load();
                video.play();
            })
            .catch(function(){
                 alert("Something went wrong")
            })
        }
    })
    .catch(function(){
        alert("Something went wrong")
    });
}