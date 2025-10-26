# Bengaluru House Price Prediction

This project predicts house prices in Bengaluru using machine learning. It provides price estimates based on property features such as location, square footage, number of bedrooms (BHK), and bathrooms. The project includes a Python backend, a trained model, and a web interface for user interaction.

## Project Overview

The project workflow includes:

1. **Data Collection** – Using raw Bengaluru housing data.  
2. **Data Cleaning & Preprocessing** – Removing noise and handling missing values.  
3. **Model Training** – Using machine learning algorithms to train a predictive model.  
4. **Prediction & Web Interface** – Users can input property details and receive price predictions.  

## Dataset

- **Source:** Kaggle (Bengaluru House Price Dataset)  
- **Raw Data:** `data/raw_data.csv`  
- **Cleaned Data:** `data/cleaned_data.csv`  

**Key Features:**
- `location` – Location of the house  
- `size` – Size in square feet  
- `total_sqft` – Total area in square feet  
- `bath` – Number of bathrooms  
- `balcony` – Number of balconies  
- `price` – House price (target variable)  

## Technologies & Algorithms

- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn  
- **Web Framework:** Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **Machine Learning Algorithm:** Linear Regression  

## Key Files and Folders

Bangalore_House_Price_Prediction/
├── client/                  # Frontend files
│   ├── app.html
│   ├── app.css
│   └── app.js
├── data/                    # Dataset files
│   ├── raw_data.csv
│   └── cleaned_data.csv
├── server/                  # Backend scripts
│   ├── server.py
│   └── util.py
├── website_images/          # Images for the website
│   └── homepage.png
├── Bangalore_House_Data.ipynb  # Notebook for data cleaning and exploration
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
 

## How It Works

1. Clean and preprocess the raw dataset using `Bangalore_House_Data.ipynb`.  
2. Train the machine learning model using the cleaned dataset (`server.py` and `util.py`).  
3. Serve predictions via the Flask backend.  
4. Users interact with the model through the frontend (`client/app.html`) to get house price estimates.  

## Purpose

- Provide accurate house price predictions for buyers, sellers, and real estate professionals.  
- Show how property features like location and size influence house pricing.  

## Author

**Surabhi H R**  
