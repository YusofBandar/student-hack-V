var text;
var score= "";

var canvas=document.getElementById("myCanvas"); //create variable for canvas
var ctx=canvas.getContext("2d");
var trumpButton=document.getElementById("trumpButton");
var scoreButton=document.getElementById("scoreButton");
var twitterbutton = document.getElementById("twitterButton"); 
var facebookbutton = document.getElementById("facebookButton"); 
var instabutton = document.getElementById("instaButton"); 
var webbutton = document.getElementById("webButton"); 
var img1 = new Image();

trumpButton.addEventListener("click", analyseText);
twitterbutton.addEventListener("click",twitter);
facebookbutton.addEventListener("click",facebook);
instabutton.addEventListener("click",instagram);
webbutton.addEventListener("click",website);

function website()
{
    var win = window.open("http://b23ce867.ngrok.io/static/desktop/index.html", '_blank');
    win.focus();
}

function instagram()
{
    var win = window.open("https://www.instagram.com/realdonaldtrump/?hl=en", '_blank');
    win.focus();
}

function twitter()
{
    var win = window.open("https://twitter.com/realDonaldTrump", '_blank');
    win.focus();
}

function facebook()
{
    var win = window.open("https://www.facebook.com/DonaldTrump/", '_blank');
    win.focus();
}


img1.src = "USAFlag.png";

img1.onload = function () {
            ctx.drawImage(img1,0, 0);
    }
    

function analyseText()
{
    text  = document.getElementById("output").value;
    text = text.split(" ").join("%20");
    
    var HTTPreq = new XMLHttpRequest(); 
    HTTPreq.open("GET","http://b23ce867.ngrok.io/?sentence=" + text,false);
    HTTPreq.send();
    var response = HTTPreq.responseText;
    console.log(response);
    var object = JSON.parse(response);
    score = object.result;
    
    scoreButton.innerHTML = score+"/10";
    sounds();
}

function sounds()
{
    if(score<=1)
        {
            var audio = new Audio('speech/donaldTrump0-1.mp3');
            audio.play();
        }
    else if(score<=3)
        {
            var audio = new Audio('speech/donaldTrump2-3.mp3');
            audio.play();
        }
    else if(score<=5)
        {
            var audio = new Audio('speech/donaldTrump4-5.mp3');
            audio.play();
        }
    else if(score<=7)
        {
            var audio = new Audio('speech/donaldTrump6-7.mp3');
            audio.play();
        }
    else
        {
            var audio = new Audio('speech/donaldTrump8.mp3');
            audio.play();
        }
    
}


chrome.tabs.executeScript( {
    code: "window.getSelection().toString();"
  }, function(selection) {
  document.getElementById("output").value = selection[0];
   //document.getElementById("word").innerHTML = selection[0];
  });



