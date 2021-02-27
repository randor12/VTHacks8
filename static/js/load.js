/**
 * Send the data to be loaded 
 * @param {string} company company being checked 
 */
function load_data(company) {
    data = {
        'company': company
    }
    $.ajax({
        dataType: "json",
        url: '/load',
        type: "POST",
        data: data,
        success: function() {
            console.log('Retrieved Data')
            window.location.href = '/display';
        },
        error: function() {
            window.location.href = '/'
        }
        
    })
}