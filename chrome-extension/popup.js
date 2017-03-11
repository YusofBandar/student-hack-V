var text;
var score = "10";

var canvas=document.getElementById("myCanvas"); //create variable for canvas
var ctx=canvas.getContext("2d");
var button=document.getElementById("myButton");
var scoreButton=document.getElementById("myButton2");

button.addEventListener("click", analyseText);

function analyseText()
{
    console.log("hit");
}


chrome.tabs.executeScript( {
    code: "window.getSelection().toString();"
  }, function(selection) {
  document.getElementById("output").value = selection[0];
   //document.getElementById("word").innerHTML = selection[0];
    text  = document.getElementById("output").value;
  });



