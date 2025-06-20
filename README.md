# Crypto News Sentiment Analysis

## Simple Overview  
A reproducible end-to-end pipeline that ingests, preprocesses, and models crypto news articles for sentiment classification, with model tracking via MLflow and production serving instrumented by Prometheus.

---

## Description  
This project uses the [Crypto News +](https://www.kaggle.com/datasets/oliviervha/crypto-news) dataset (Oct 2021–Dec 2023), which includes titles, full text, source, subject, and TextBlob sentiment scores. We parse and clean the text, perform EDA, vectorize with TF-IDF, and train a binary sentiment classifier (Logistic Regression). Experiments and metrics (accuracy, precision, recall, ROC AUC, F1) are tracked in MLflow. A CI/CD workflow via GitHub Actions (MLflow Project + `conda.yaml`) automates retraining, and a Flask/FastAPI service exposes a `/predict` endpoint with Prometheus metrics scraped by Grafana dashboards and alerting rules.

---

## Getting Started

### Dependencies  
- **OS:** Windows 10 / macOS Catalina+ / Ubuntu 20.04+  
- **Python:** ≥ 3.8  
- **Libraries:**  
  - pandas, numpy  
  - scikit-learn  
  - nltk (or spaCy)  
  - mlflow  
  - flask or fastapi  
  - prometheus_client  
  - uvicorn (for FastAPI)  
  - requests (for inference script)

### Installing  
1. **Clone repository**  
   git clone https://github.com/your-username/crypto-news-sentiment.git
   cd crypto-news-sentiment

2. **Create & activate virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate       # Windows
   ```
3. **Install requirements**

   ```bash
   pip install -r requirements.txt
   ```

---

## Executing Program

1. **Preprocess data**

   ```bash
   python preprocessing/automate_crypto_preprocessing.py \
     --input data/crypto_news_raw.csv \
     --output data/crypto_news_clean.csv \
     --vectorizer artifacts/vectorizer.pkl
   ```
2. **Train & track model**

   ```bash
   cd Membangun_model
   mlflow run . -P data_path=../data/crypto_news_clean.csv
   ```
3. **Run inference service**

   ```bash
   # Start API (Flask)
   flask run --port 5000

   # or FastAPI
   uvicorn app:app --reload --port 8000
   ```
4. **Test prediction**

   ```bash
   python inference.py --text "Bitcoin surges after ETF approval"
   ```

---

## Model Performance

*(as logged in MLflow)*

* **Accuracy:** 0.829
* **Precision:** 0.846
* **Recall:** 0.829
* **ROC AUC:** 0.905
* **Test F1:** 0.828
* **Training Time:** 83.17 s

---

## Help

* **NLTK data missing:**

  ```python
  import nltk
  nltk.download('punkt')
  nltk.download('stopwords')
  ```
* **MLflow UI not showing runs:**

  ```bash
  mlflow ui --backend-store-uri ./mlruns
  ```
* **View API options:**

  ```bash
  python app.py --help
  ```

---

## Authors

* Dominique Pizzie – [d.pizzie@example.com](mailto:d.pizzie@example.com)
* @DomPizzie

---

## Version History

* **0.2**

  * Added CI/CD with GitHub Actions
  * Integrated Prometheus/Grafana monitoring & alerting
* **0.1**

  * Initial release: preprocessing, modelling, serving

---

## License

This project is licensed under the MIT License – see the [LICENSE.md](LICENSE.md) file for details.

---

## Acknowledgments

* [Crypto News + dataset](https://www.kaggle.com/datasets/oliviervha/crypto-news)
* TextBlob examples for sentiment analysis
* Mermaid flowchart snippets by PurpleBooth
* MLflow docs by dbader
* Grafana patterns by zenorocha
* Prometheus exporter guides by fvcproductions

```

Let me know if you’d like any tweaks!
```
