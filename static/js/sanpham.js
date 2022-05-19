function anthongbaotvgh() {
    document.getElementById("tvgh-tc").style.display = "none";
}

var x = document.getElementsByClassName("btn-tvgh");
var i;
for (i = 0; i < x.length; i++) {
    x[i].onclick = function() {
        themvaogiohang_sp(this);
        document.getElementById("tvgh-tc").style.display = "block";
        setTimeout(anthongbaotvgh, 1000);
    }
}