# California Housing Price Predictor API

This is a simple and efficient API built with **FastAPI** to predict the total number of bedrooms in a California housing district based on several input features. The prediction is made using a pre-trained linear regression model.

## 🚀 Features

* **Fast & Efficient**: Built on top of FastAPI for high performance.
* **Easy to Use**: Simple and intuitive API endpoints.
* **Interactive Docs**: Automatic, interactive API documentation powered by Swagger UI and ReDoc.
* **Health Check**: A root endpoint to quickly verify if the API is running.

## 📋 Prerequisites

Before you begin, ensure you have Python 3.7+ installed. You will also need the following libraries:

* `fastapi`
* `uvicorn`
* `pandas`
* `scikit-learn`

Additionally, you must have the trained model file `linear_reg_model.pkl` in the same directory as `main.py`.

## ⚙️ Installation & Setup

1.  **Clone the repository (or download the files):**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-directory>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    Create a `requirements.txt` file with the following content:
    ```
    fastapi
    uvicorn[standard]
    pandas
    scikit-learn
    ```
    Then, run the installation command:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Place the model file:**
    Ensure your trained model file, `linear_reg_model.pkl`, is in the root directory of the project.

## ▶️ Running the Application

To start the API server, run the following command in your terminal:

```bash
uvicorn main:app --reload