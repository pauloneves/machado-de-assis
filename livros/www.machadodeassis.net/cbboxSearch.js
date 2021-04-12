var _str = "";
var _timeout = 0;

function cbboxSearch(sel, e) {
    var i=0, c=true;
    _str = _str + String.fromCharCode(e.keyCode);
    _str = _str.toLowerCase();
    while (c) {
        var textOpt = sel.options[i].text.toLowerCase();
        var strOpt = textOpt.substr(0, (_str.length));
        if (strOpt == _str) {
            sel.options[i].selected = true;
            c = false;
        }
        if (i >= (sel.options.length - 1)) {
            c = false;
        }
        i++;
    }
    clearTimeout(_timeout);
    _timeout = setTimeout("cbboxSearchRestart()", 2000);
}

function cbboxSearchRestart() {
    clearTimeout(_timeout);
    _str = "";
}

