import os
import json
import pickle
import numpy as np

__data_columns = None
__locations = None
__model = None

def load_saved_artifacts():
    global __data_columns
    global __locations
    global __model

    print("Loading saved artifacts...")

    columns_path = r"C:\Users\HP\Bengaluru_House_Data\Bangalore_House_Price\artifacts\columns.json"
    model_path = r"C:\Users\HP\Bengaluru_House_Data\Bangalore_House_Price\artifacts\model.pkl"

    with open(columns_path, "r", encoding='utf-8') as f:
        data = json.load(f)
        __data_columns = data.get("data_columns") or data.get("columns") or data

    # Locations are all columns after first 3 numeric column
    __locations = __data_columns[3:]

    # Load model
    with open(model_path, "rb") as f:
        __model = pickle.load(f)

    print("Artifacts loaded successfully!")
    print("Total locations loaded:", len(__locations))
    print("Sample locations:", __locations[:20])


def get_location_names():
    if __locations is None:
        return []
    return __locations


def get_estimated_price(location, total_sqft, bhk, bath):
    if __data_columns is None or __model is None:
        raise Exception("Artifacts not loaded. Please call load_saved_artifacts() first.")

    x = np.zeros(len(__data_columns))
    x[0] = float(total_sqft)
    x[1] = float(bath)
    x[2] = float(bhk)

    if location in __data_columns:
        loc_index = __data_columns.index(location)
        x[loc_index] = 1
    else:
        print(f"Warning: location '{location}' not found. Using default zeros for location.")

    return round(__model.predict([x])[0], 2)


if __name__ == "__main__":
    load_saved_artifacts()
    print("All locations loaded:", get_location_names())
    print("Estimated price:", get_estimated_price("1st Phase JP Nagar", 1000, 3, 3))
