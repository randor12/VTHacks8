/**
 * Send the vals to be loaded
 * @param {string} componies and stock prices
 */
function fix_box(vals) {
    console.log("Function called");
    console.log(vals)
    var list = vals.split(",")
    var names = new Array()
    var prices =  new Array()
    for (var i = 0 ; i < list.length / 2; i++){
        var k = i * 2
        names.push(list[k]);
        prices.push(list[k+1])
        console.log(list[k])
    }
    var cols =  document.getElementsByClassName("col");
    console.log(cols)
    for (var i = 0; i < 3; i ++){
        console.log("trying to change values")
        cols[i].getElementsByClassName("StockLabel")[0].getElementsByTagName("text")[0].innerHTML = "gme"
        cols[i].getElementsByClassName("card-body")[0].innerHTML = "Stock Price is: "
        console.log(names[i])
    }


}