document.getElementById("mota").onclick = function() {
    document.getElementById("mota-sp").style.display = "block";
    document.getElementById("mota").style.textDecoration = "underline";
    document.getElementById("mota").style.color = "black";
    document.getElementById("danhgia-sp").style.display = "none";
    document.getElementById("danhgia").style.textDecoration = "none";
    document.getElementById("danhgia").style.color = "darkgray";
}

document.getElementById("danhgia").onclick = function() {
    document.getElementById("mota-sp").style.display = "none";
    document.getElementById("mota").style.textDecoration = "none";
    document.getElementById("mota").style.color = "darkgray";
    document.getElementById("danhgia-sp").style.display = "block";
    document.getElementById("danhgia").style.textDecoration = "underline";
    document.getElementById("danhgia").style.color = "black";
}

function anthongbaotvgh() {
    document.getElementById("tvgh-tc").style.display = "none";
}

document.getElementById("btn-tvgh").onclick = function() {
    document.getElementById("tvgh-tc").style.display = "block";
    themvaogiohang_ctsp(this);
    setTimeout(anthongbaotvgh, 1000);
}

// document.getElementById("btn-mn").onclick = function() {
//     themvaogiohang_ctsp(this);
//     location.href = "{% url 'dathang' %}";
// }