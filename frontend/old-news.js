const cards2 = document.querySelector(".container");

document.getElementById("more-news").onclick = function() {myFunction()};

function myFunction(){

let obj = new XMLHttpRequest();
obj.open('get', 'http://127.0.0.1:8000/get_old_news');
obj.send();
obj.onload = function () {
    
    var x = obj.response;
    var y = JSON.parse(x);
    for (var i = 0; i < y.length; i++) {
        let card = `<div class="card">
            <div class="row row1">${y[i]["category"][0].toUpperCase()}</div>
            <div class="row row2">${y[i]["title"]}</div>
            <div class="row row3">
                <p>${y[i]["description"]}</p>
            </div>
            <div class="row">
                <div class="col">${y[i]["pubdate"]}</div>
                <div class="col col2">${y[i]["source_id"].toUpperCase()}</div>
                <div class="col col2">${y[i]["country"][0].toUpperCase()}</div>
            </div>
            <div class="row">
                <div><a href="${y[i]["link"]}" target="_blank"> Click Here to see detail</a></div>
            </div>
        </div>`;
        cards2.innerHTML += card;
    }
   

};
}