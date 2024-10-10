var writeup = document.getElementsByTagName("link")[0].import;
var absatz = writeup.getElementsByTagName("p")[0];
window.addEventListener("load", function() {
document.getElementsByTagName("body")[0].replaceChild(writeup.getElementsByTagName("body")[0], document.getElementsByID("writeup")[0]);
}, false);
