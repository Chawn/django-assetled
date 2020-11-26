document.getElementsByClassName("bts-popup-close")[0].click();

var val = "41";  //41 = จ.อุดรธานี
var sel = document.getElementById('ddlProvince');

var opts = sel.options;
for (var opt, j = 0; opt = opts[j]; j++) {
    if (opt.value == val) {
        sel.selectedIndex = j;
        break;
    }
}
myPostBackProvince();

function myPostBackProvince() {
    Sys.WebForms.PageRequestManager.getInstance().add_endRequest(clearPostBackProvince);
    __doPostBack('ddlProvince', '');
    
}

function clearPostBackProvince(){
    $get('__EVENTTARGET').value = $get('__EVENTARGUMENT').value = '';
    Sys.WebForms.PageRequestManager.getInstance().remove_endRequest(clearPostBackProvince);

    setAmpur();
}

function setAmpur() { 

    var val2= "01"; //01 = อ.เมือง
    var sel2 = document.getElementById('ddlAmphur');
    
    var opts2 = sel2.options;
    for (var opt, j = 0; opt = opts2[j]; j++) {
        if (opt.value == val2) {
            sel2.selectedIndex = j;
            break;
        }
    }
    myPostBackAmpur();
}

function myPostBackAmpur() {
    Sys.WebForms.PageRequestManager.getInstance().add_endRequest(clearPostBack);
    __doPostBack('ddlAmphur', '');
}

function clearPostBack() {
    $get('__EVENTTARGET').value = $get('__EVENTARGUMENT').value = '';
    Sys.WebForms.PageRequestManager.getInstance().remove_endRequest(clearPostBack);

    // TODO: anything you want after __doPostBack

    document.getElementById('txtPacelNo').value = "171367" ;
    document.getElementById('btnFind').click() ;
}

