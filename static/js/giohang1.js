var gh = sessionStorage.getItem("giohang");
var giohang = JSON.parse(gh);
if(giohang == null) giohang = new Array;

// giohang.push(new Array("../../static/images/bantra.jpg", "Bàn trà bt04","960000","1" ) );
// giohang.push(new Array("../../static/images/bantra.jpg", "Bàn trà bt04","960000","1" ) );
// giohang.push(new Array("../../static/images/bantra.jpg", "Bàn trà bt04","960000","1" ) );


capnhatslgiohang();

function luugiohang() {
    sessionStorage.setItem("giohang", JSON.stringify(giohang));
}

function capnhatslgiohang() {
    var t_sosp = document.getElementById("sosp").children;
    t_sosp[0].innerHTML = giohang.length;
}



function capnhatspgiohang() {
    var ptu_html = '';
    if(giohang.length == 0) {
        document.getElementsByClassName("DatHang")[0].style.display = "none";
        return;
    }
    for(var i = 0; i < giohang.length; i++) {
        ptu_html +=
        '<tr>' +
            '<td class="xoa-sp">' +
                '<button class="div-xoa-sp" onclick="xoasanpham(this, '+ i +')">X</button>' +
            '</td>' +
            '<td class="anh-sp"><img src="' + giohang[i][0] + '"></td>' +
            '<td class="ten-sp"><p>' + giohang[i][1] +'</p></td>' +
            '<td class="gia-sp">' + giohang[i][2] +'</td>' +
            '<td class="sl-sp">' +
                '<input class="btn-g input" onclick="giamsoluong(this, '+ i +')" value="-" type="button">' +
                '<input class="input-sl input" disabled min="0" max="20" name="sl" type="text" value="' + giohang[i][3] + '">' +
                '<input class="btn-t input" onclick="tangsoluong(this, '+ i +')" type="button" value="+">' +
            '</td>' +
            '<td class="sotien-sp">' + (giohang[i][2] * giohang[i][3]) +'</td>' +
        '</tr>';
    }
    ptu_html +=
        '<tr>' +
            '<td colspan="5" id="tongcong">Tổng cộng:</td>' +
            '<td class="sotien-sp"></td>' +
        '</tr>';
    document.getElementById("sp-gh").innerHTML += ptu_html;
    //alert(document.getElementById("sp-gh").innerHTML);
    capnhattongtien();
}


function themvaogiohang_sp(x) {
    var child =  x.parentElement.parentElement.children;
    var src = child[0].src;
    var tensp = child[1].innerText;
    var giasp = child[2].innerText;
    var idsp = child[4].innerText;
    giasp = parseInt(giasp.replace(' VNĐ', ''));
    var sl = 1;
    var themmoi = 1;
    for (var i = 0; i < giohang.length; i++) {
        if(giohang[i][0] == src & giohang[i][1] == tensp & giohang[i][2] == giasp & giohang[i][4] == idsp) {
            themmoi = 0;
            giohang[i][3] += 1;
            break;
        }
    }

    if (themmoi == 1) giohang.push(new Array(src, tensp, giasp, sl, idsp));
    
    capnhatslgiohang();
    luugiohang();
}



function themvaogiohang_ctsp(x) {
    var child =  x.parentElement.parentElement.parentElement.children;
    var src = child[0].children[0].src;
    child = child[1].children;
    var tensp = child[0].innerText;
    var giasp = child[1].innerText;
    var idsp = child[5].innerText;
    giasp = parseInt(giasp.replace(' VNĐ', ''));
    var sl = 1;
    var themmoi = 1;
    for (var i = 0; i < giohang.length; i++) {
        if(giohang[i][0] == src & giohang[i][1] == tensp & giohang[i][2] == giasp & giohang[i][4] == idsp) {
            themmoi = 0;
            giohang[i][3] += 1;
            break;
        }
    }
    if (themmoi == 1) giohang.push(new Array(src, tensp, giasp, sl, idsp));
    
    capnhatslgiohang();
    luugiohang();
}

function tongtiendonhang() {
    var tongcong = parseInt('0');
    for(var i = 0; i < giohang.length; i++) {
        var sotien = giohang[i][2] * giohang[i][3];
        tongcong = tongcong + parseInt(sotien);
    }
    document.getElementById("tth").innerText = tongcong;
    document.getElementById('id_tienhang').setAttribute('value', tongcong);

    var pvc = 0;
    if(tongcong < 1000000) {
        pvc = 100000;
        tongcong += pvc;
    }

    document.getElementById("ps").innerText = pvc;
    document.getElementById('id_phivanchuyen').setAttribute('value', pvc);

    document.getElementById("tst").innerText = tongcong;
    document.getElementById('id_tongtien').setAttribute('value', tongcong);
}