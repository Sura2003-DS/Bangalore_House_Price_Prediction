function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for (var i = 0; i < uiBathrooms.length; i++) {
        if (uiBathrooms[i].checked) {
            return parseInt(uiBathrooms[i].value);
        }
    }
    return -1;
}

function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for (var i = 0; i < uiBHK.length; i++) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1;
}

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");

    var sqft = document.getElementById("uiSqft").value.trim();
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations").value;
    var estPrice = document.getElementById("uiEstimatedPrice");

    // Validate input
    if (!sqft || isNaN(sqft) || parseFloat(sqft) <= 0 || !location || bhk <= 0 || bathrooms <= 0) {
        estPrice.innerHTML = "<h2>Please fill all fields correctly!</h2>";
        return;
    }

    console.log("Sending to server:", {
        total_sqft: parseFloat(sqft),
        bhk: bhk,
        bath: bathrooms,
        location: location
    });

    var url = "http://127.0.0.1:5000/predict_home_price";

    $.ajax({
        url: url,
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({
            total_sqft: parseFloat(sqft),
            bhk: bhk,
            bath: bathrooms,
            location: location
        }),
        success: function(data) {
            if (data.error) {
                estPrice.innerHTML = "<h2>Error: " + data.error + "</h2>";
                console.error(data.error);
            } else {
                estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakh</h2>";
                console.log("Estimated price:", data.estimated_price);
            }
        },
        error: function(err) {
            estPrice.innerHTML = "<h2>Server Error</h2>";
            console.error("AJAX Error:", err);
        }
    });
}

function onPageLoad() {
    console.log("Document loaded");

    var url = "http://127.0.0.1:5000/get_location_names";

    $.get(url, function(data, status) {
        console.log("got response for get_location_names request", data);
        if (data && data.locations) {
            var uiLocations = $('#uiLocations');
            uiLocations.empty(); // clear existing options
            uiLocations.append(new Option("Choose a Location", "")); // default placeholder

            for (var i = 0; i < data.locations.length; i++) {
                uiLocations.append(new Option(data.locations[i], data.locations[i]));
            }
        } else {
            console.error("No locations found in response");
        }
    }).fail(function(err) {
        console.error("Failed to load locations:", err);
    });
}

window.onload = onPageLoad;
