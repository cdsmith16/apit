var execute = function() {
    //apiform = document.getElementById("apiform");
    infoload();
    // Handler when the DOM is fully loaded
    //console.log('executed');
};

function infoload() {
    event.preventDefault();
    //console.log('started tag function');
    //set variables
    var fqtag = document.createElement("script");
    let p = window.location.href;
    let a = navigator.userAgent;
    let cmp = "Christian";
    let fqurl = `//c.fqtag.com/tag/implement-r.js?org=BB6DvPmytpFndg8atDcN&p=${p}&a=${a}&cmp=${cmp}&fmt=banner&rt=display&sl=1&fq=1`;
    //confirm url is set
    console.log(fqurl);
    fqtag.src = fqurl;
    fqtag.async = true;
    fqtag.type = "text/javascript";
    fqtag.id = "fqtag";
    //append script, firing tag
    document.head.appendChild(fqtag);
    return false;
}

if (
    document.readyState === "complete" ||
    (document.readyState !== "loading" && !document.documentElement.doScroll)
) {
    execute();
} else {
    document.addEventListener("DOMContentLoaded", execute);
}
