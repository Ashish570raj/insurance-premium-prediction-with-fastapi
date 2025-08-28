
# Insurance Premium Prediction with FastAPI

## Introduction

This project is a **Machine Learning application** built using **FastAPI** that predicts insurance premiums based on customer details such as age, gender, BMI, smoking habits, and region. The backend is powered by FastAPI, making it lightweight, fast, and easy to deploy, while the model is trained on historical insurance data.

The application can be accessed via REST API endpoints as well as a simple UI for interaction.

---

## Table of Contents

* [Features](#features)
* [Project Structure](#project-structure)
* [Installation](#installation)
* [API Endpoints](#api-endpoints)
* [Example](#example)
* [Dependencies](#dependencies)
* [Contributors](#contributors)
* [License](#license)

---

## Features

* Predict insurance premium using trained ML model.
* REST API built with **FastAPI**.
* Input validation with Pydantic schema.
* Interactive Swagger UI (`/docs`) and Redoc UI (`/redoc`).
* CSV dataset (`insurance.csv`) included for training and testing.
* User interface script (`ui.py`) for easy local use.

---

## Project Structure

```bash
insurance-premium-prediction-with-fastapi/
│── Config/
│   ├── city_tire.py        # Configuration settings
│   └── insenv              # Environment settings
│
│── model/
│   ├── model.pkl           # Trained ML model
│   ├── predict.py          # Prediction logic
│   └── prediction.ipynb    # Jupyter notebook (model training & analysis)
│
│── Schema/
│   ├── UserInput.py        # Input schema
│   └── predicion_response.py # Response schema
│
│── insurance.csv           # Dataset
│── main.py                 # FastAPI entry point
│── ui.py                   # UI for interacting locally
│── requirements.txt        # Dependencies
│── Dockerfile              # Docker setup
│── note.txt                # Notes/documentation
│── .gitignore
│── Readme.md               # Project documentation

```
---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Ashish570raj/insurance-premium-prediction-with-fastapi.git
   cd insurance-premium-prediction-with-fastapi
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

---

## API Endpoints

| Method | Endpoint   | Description      |
| ------ | ---------- | ---------------- |
| GET    | `/`        | Home endpoint    |
| GET    | `/health`  | Health check API |
| POST   | `/predict` | Predict premium  |

---

## Example

**Request (POST /predict):**

```json
{
  "age": 35,
  "weight": 70,
  "height": 170,
  "income_lpa": 12,
  "smoker": false,
  "city": "Bangalore",
  "occupation": "Software Engineer"
}
```

**Response (200 OK):**

```json
{
  "Predicted_category": "High",
  "confidence": 0.8432,
  "class_probabilities": {
    "High": 0.84,
    "Low": 0.01,
    "Medium": 0.15
  }
}
```
---

## Dependencies

All dependencies are listed in `requirements.txt`. Key libraries include:

* FastAPI
* Uvicorn
* Pydantic
* Scikit-learn
* Pandas
* Numpy

---

## Contributors

* **Ashish Raj** 

---

## License

This project is licensed under the MIT License.

---
