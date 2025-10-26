from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    try:
        print("Getting location names...")
        locations = util.get_location_names()
        print(f"Locations found: {len(locations)}")
        return jsonify({'locations': locations})
    except Exception as e:
        print(f"Error getting locations: {str(e)}")
        return jsonify({'error': str(e)})

@app.route('/predict_home_price', methods=['POST', 'OPTIONS'])
def predict_home_price():
    if request.method == 'OPTIONS':
        print("Handling OPTIONS preflight request")
        return '', 200
        
    try:
        print("Received POST request for price prediction")
        
        if not request.is_json:
            print("Request is not JSON")
            return jsonify({'error': 'Request must be JSON'}), 400
            
        data = request.get_json()
        print(f"Request data: {data}")
        
        total_sqft = float(data.get('total_sqft', 0))
        location = data.get('location', '')
        bhk = int(data.get('bhk', 0))
        bath = int(data.get('bath', 0))

        print(f"Parsed values - Location: {location}, Sqft: {total_sqft}, BHK: {bhk}, Bath: {bath}")

        if not location or location == "" or location == "Choose a Location":
            print("Invalid location")
            return jsonify({'error': 'Please select a valid location'}), 400
            
        if total_sqft <= 0:
            print("Invalid square footage")
            return jsonify({'error': 'Please provide valid square footage'}), 400
            
        if bhk <= 0:
            print("Invalid BHK")
            return jsonify({'error': 'Please select valid BHK'}), 400
            
        if bath <= 0:
            print("Invalid bathroom count")
            return jsonify({'error': 'Please select valid number of bathrooms'}), 400

        print(f"Calling util.get_estimated_price...")
        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
        
        print(f"Estimated price: {estimated_price}")
        
        return jsonify({'estimated_price': estimated_price})

    except Exception as e:
        print(f"Error in predict_home_price: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    print("Server ready on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)