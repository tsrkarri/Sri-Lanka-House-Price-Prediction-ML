# TEJESWARA SAI REDDY KARRI (TP062689) APD3F2302CS(DA)
import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None
__scaler = None
__price_scaler = None

def price_predict(baths, land_size, beds, house_size, location):
    try:
        # Convert the location to lowercase to ensure case insensitivity
        location = location.lower()
        loc_index = __data_columns.index(location)
    except ValueError:
        # Handle the case where the location is not found
        loc_index = -1

    if loc_index != -1:
        # Hold the scaled input features
        scaled_features = np.zeros(len(__data_columns))

        # Set the non-numerical attributes
        scaled_features[loc_index] = 1  # Set the location index

        # Scale the numerical input values
        scaled_numerical_features = __scaler.transform([[baths, land_size, beds, house_size]])

        # Replace the corresponding positions in the scaled_features array with scaled numerical values
        scaled_features[0:4] = scaled_numerical_features

        scaled_output = __model.predict([scaled_features])[0]

        # Inverse transform the scaled output to get the original scale
        unscaled_output = __price_scaler.inverse_transform([[scaled_output]])

        return round(unscaled_output[0][0], 2)
    else:
        # Handle the case where location is not found
        return "Location not found in the dataset"


def get_location_names():
    load_saved_artifacts()
    return __locations

def load_saved_artifacts():
    print(" STATUS : STARTED - loading saved artifacts...")
    global __data_columns
    global __locations

    with open('../model/columns.json', 'r') as f:
        __data_columns = json.load(f)['data columns']
        __locations = __data_columns[4:]
    global __model
    with open("../model/fyp_model.pickle", 'rb') as g:
        __model = pickle.load(g)

    global __scaler
    with open("../model/scaler.pickle", 'rb') as h:
        __scaler = pickle.load(h)

    global __price_scaler
    with open("../model/price_scaler.pickle", 'rb') as k:
        __price_scaler = pickle.load(k)

    print("STATUS : COMPLETED - loading artifacts done ....")

if __name__ == '__main__':
    load_saved_artifacts()
# #     print(get_location_names())
    print(price_predict(4, 5788, 5, 3480, ' athurugiriya,  colombo'))
    print(price_predict(4, 5788, 5, 3480, ' akuressa,  matara'))
