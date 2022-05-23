// Replaces or appends URL currency parameter to the url without overwriting other URL parameters
let select = document.querySelector("select");

select.addEventListener("change", (e) => {
    let param = `?currency=${e.target.value.toUpperCase()}`;
    if (window.location.search.match(/[\?|\&]currency=/i)) {
        // will replace existing currency URL param that is set with new currency value
        window.location.search = window.location.search.replace(/[\?|\&]currency=[A-Za-z]+/i, param);
    } else {
        window.location.search += param;
    }
})

// If the URL currency parameter is set it will update the select with the correct value
if (window.location.search.match(/[\?|\&]currency/i)) {
    select.value = window.location.search.split("?currency=")[1].split(/\&|\?/)[0];
}