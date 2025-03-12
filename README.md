# Customer Churn Prediction

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![React Version](https://img.shields.io/badge/react-18.2.0-blue)](https://reactjs.org/)

Customer churn prediction is a machine learning project aimed at identifying customers who are likely to churn (i.e., stop using your service) based on historical data. This repository contains the code for training the predictive model using Python and deploying it with FastAPI for interaction with a React.js frontend.

## Table of Contents

- [Customer Churn Prediction](#customer-churn-prediction)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)

## Features

- Train machine learning models to predict customer churn.
- Expose the trained models via a FastAPI backend.
- Interact with the prediction model using a React.js frontend.

## Installation

To set up this project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/thekavikumar/customer-churn-prediction.git
   cd customer-churn-prediction
   ```

2. Install the required Python dependencies:

   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Install the required Node.js dependencies for the React.js frontend:

   ```bash
   cd frontend
   npm install
   ```

## Usage

1. Train the machine learning model using your dataset. See `train_model.ipynb` for an example notebook.
2. Run the FastAPI backend:

   ```bash
   uvicorn app.main:app --reload
   ```

3. Start the React.js frontend:

   ```bash
   cd frontend
   npm start
   ```

4. Open your web browser and navigate to `http://localhost:3000` to use the application.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

Feel free to customize this template to better fit your project. Let me know if you need further assistance!
