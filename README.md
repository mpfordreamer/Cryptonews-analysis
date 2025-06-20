# 📈 Crypto News Sentiment Analysis
![ChatGPT Image 18 Jun 2025, 14 43 47](https://github.com/user-attachments/assets/ff455ee6-6c31-406b-bd02-0b4e2cf43557)

An end-to-end MLOps pipeline for classifying sentiment in crypto news, complete with experiment tracking using MLflow and production monitoring with Prometheus & Grafana.

![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

</div>

---

## 📝 Description

This project builds a complete pipeline to process crypto news data, from ingestion and preprocessing to deploying the model as an API service. Using the [Crypto News +](https://www.kaggle.com/datasets/oliviervha/crypto-news) dataset, we train a sentiment classification model (Positive/Negative) and package it into a production-ready MLOps workflow.

---

## ✨ Key Features

-   **🧹 Data Preprocessing**: Cleans and prepares news text for modeling.
-   **🤖 Model Training**: Uses TF-IDF and Logistic Regression for sentiment classification.
-   **📊 Experiment Tracking**: Logs all parameters, metrics, and model artifacts to **MLflow**.
-   **🚀 API Deployment**: Serves the model via a `/predict` endpoint using **Flask/FastAPI**.
-   **⚙️ CI/CD Automation**: A **GitHub Actions** workflow for automated model retraining and validation.
-   **📡 Production Monitoring**: API performance metrics are exposed for **Prometheus** and visualized in **Grafana**.

---

## 🛠️ Tech Stack

-   **Data & Modeling**: `pandas`, `scikit-learn`, `nltk`
-   **MLOps**: `MLflow`
-   **Serving**: `Flask`, `FastAPI`, `Uvicorn`
-   **Monitoring**: `Prometheus`, `Grafana`
-   **Automation**: `GitHub Actions`

---

## 🚀 Getting Started

### System Requirements

-   **OS**: Windows 10 / macOS Catalina+ / Ubuntu 20.04+
-   **Python**: Version `3.8` or higher

### Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/crypto-news-sentiment.git
    cd crypto-news-sentiment
    ```

2.  **Create and Activate Virtual Environment**
    ```bash
    # Create environment
    python -m venv venv

    # Activate on macOS/Linux
    source venv/bin/activate

    # Activate on Windows
    venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

---

## ⚙️ How to Run

Follow these steps in order:

1.  **Run Data Preprocessing**
    This command will clean the raw data and save the result along with the vectorizer.
    ```bash
    python preprocessing/automate_crypto_preprocessing.py \
      --input data/crypto_news_raw.csv \
      --output data/crypto_news_clean.csv \
      --vectorizer artifacts/vectorizer.pkl
    ```

2.  **Train and Track the Model with MLflow**
    Navigate to the model directory and run the MLflow pipeline.
    ```bash
    cd Membangun_model
    mlflow run . -P data_path=../data/crypto_news_clean.csv
    ```
    *To see the results, run `mlflow ui` in your terminal.*

3.  **Run the API Service**
    Choose one of the frameworks to run the server.

    ```bash
    # Option 1: Using Flask
    flask run --port 5000

    # Option 2: Using FastAPI
    uvicorn app:app --reload --port 8000
    ```

4.  **Test the Prediction Endpoint**
    Send a request to the API using the inference script.
    ```bash
    python inference.py --text "Bitcoin surges after ETF approval"
    ```

---

## 📊 Model Performance

The following metrics were logged on the best run in MLflow.

| Metric          | Score   |
| --------------- | ------- |
| **Accuracy**    | `0.829` |
| **Precision**   | `0.846` |
| **Recall**      | `0.829` |
| **ROC AUC**     | `0.905` |
| **F1 Score**    | `0.828` |
| **Training Time** | `83.17s`|

---

## 🆘 Help (Troubleshooting)

-   **`NLTK data missing` error:**
    Run the following Python command to download the required data.
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    ```

-   **MLflow UI not showing runs:**
    Make sure you are running the UI from the project's root directory.
    ```bash
    mlflow ui --backend-store-uri ./mlruns
    ```

-   **Viewing script options:**
    Use the `--help` flag to see available arguments.
    ```bash
    python app.py --help
    ```

---

## ✍️ Author

-   **De Mahesta** – [dewamahesta2711@gmail.com](mailto:dewamahesta2711@gmail.com)

---

## 📜 Version History

-   **v0.2**
    -   Added CI/CD with GitHub Actions.
    -   Integrated monitoring & alerting with Prometheus/Grafana.
-   **v0.1**
    -   Initial release: preprocessing, modeling, and API serving.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

---

## 🙏 Acknowledgments

-   [Crypto News +](https://www.kaggle.com/datasets/oliviervha/crypto-news) dataset
-   [TextBlob](https://textblob.readthedocs.io/en/dev/) usage examples
-   Workflow snippets by [PurpleBooth](https://github.com/PurpleBooth)
-   MLflow docs by [dbader](https://github.com/dbader)
-   Grafana patterns by [zenorocha](https://github.com/zenorocha)
