// TEJESWARA SAI REDDY KARRI (TP062689) APD3F2302CS(DA)
function onClickPredictPrice(){
    console.log("Predict button is clicked!!!");
    var beds = document.getElementById('beds');
    var baths = document.getElementById('baths');
    var land_size = document.getElementById('land_size');
    var house_size = document.getElementById('house_size');
    var location = document.getElementById('location');
    var price_predicted = document.getElementById('price_predicted');

    // Get the current value
    var locationValue = location.value;

    // Split the value at the comma, add spaces, and then join it back
    var modifiedLocationValue = locationValue.split(',').map(function(item) {
    return ' ' + item.trim(); // Add spaces at the beginning and after the comma
    }).join(', ');

    console.log(modifiedLocationValue);

    var url = "https://tejfyp.pythonanywhere.com/predict_house_price";
    
    $.post(url, {
        beds: beds.value,
        baths: baths.value,
        land_size: parseFloat(land_size.value),
        house_size: parseFloat(house_size.value),
        location: modifiedLocationValue
    },function(data,status){
        console.log(data.price_predict);
        price_predicted.innerHTML = "<h3 class="+"text-dark"+"> Predicted Price is "+data.price_predict.toString()+" LKR </h3>";
        console.log(status);
    });

}

function onPageLoad() {
    console.log("document loaded");
    var url = "https://tejfyp.pythonanywhere.com/get_location_names";
    $.get(url,function(data,status){
        console.log("got response for location names request");
        if(data){
            console.log("got here ");
            var locations = data.locations;
            var location = document.getElementById("location");
            $('#location').empty();
            console.log("got here ");
            for(var i in locations){
                var opt = new Option(locations[i].toUpperCase());

                $('#location').append(opt);
                
            }
        }
        console.log("got here ");
    });
}

window.onload = onPageLoad();
