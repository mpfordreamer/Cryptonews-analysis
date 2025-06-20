# 📈 Analisis Sentimen Berita Kripto

**Sebuah pipeline MLOps *end-to-end* untuk klasifikasi sentimen pada berita kripto, dilengkapi dengan *experiment tracking* menggunakan MLflow dan *monitoring* produksi dengan Prometheus & Grafana.**

![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

</div>

---

## 📝 Deskripsi

Proyek ini membangun sebuah pipeline lengkap untuk mengolah data berita kripto, mulai dari ingestion, preprocessing, hingga deployment model sebagai layanan API. Menggunakan dataset [Crypto News +](https://www.kaggle.com/datasets/oliviervha/crypto-news), kami melatih model klasifikasi sentimen (Positif/Negatif) dan mengemasnya dalam sebuah alur kerja MLOps yang siap produksi.

---

## ✨ Fitur Utama

-   **🧹 Preprocessing Data**: Membersihkan dan mempersiapkan teks berita untuk pemodelan.
-   **🤖 Pelatihan Model**: Menggunakan TF-IDF dan Logistic Regression untuk klasifikasi sentimen.
-   **📊 Experiment Tracking**: Mencatat semua parameter, metrik, dan artefak model ke **MLflow**.
-   **🚀 Deployment API**: Menyajikan model melalui endpoint `/predict` menggunakan **Flask/FastAPI**.
-   **⚙️ Otomatisasi CI/CD**: Alur kerja **GitHub Actions** untuk otomatisasi *retraining* dan validasi model.
-   **📡 Monitoring Produksi**: Metrik performa API diekspos untuk **Prometheus** dan divisualisasikan di **Grafana**.

---

## 🛠️ Tumpukan Teknologi (Tech Stack)

-   **Data & Pemodelan**: `pandas`, `scikit-learn`, `nltk`
-   **MLOps**: `MLflow`
-   **Serving**: `Flask`, `FastAPI`, `Uvicorn`
-   **Monitoring**: `Prometheus`, `Grafana`
-   **Otomatisasi**: `GitHub Actions`

---

## 🚀 Memulai

### Kebutuhan Sistem

-   **OS**: Windows 10 / macOS Catalina+ / Ubuntu 20.04+
-   **Python**: Versi `3.8` atau lebih tinggi

### Instalasi

1.  **Clone Repositori**
    ```bash
    git clone https://github.com/your-username/crypto-news-sentiment.git
    cd crypto-news-sentiment
    ```

2.  **Buat dan Aktifkan Virtual Environment**
    ```bash
    # Buat environment
    python -m venv venv

    # Aktifkan di macOS/Linux
    source venv/bin/activate

    # Aktifkan di Windows
    venv\Scripts\activate
    ```

3.  **Instal Dependensi**
    ```bash
    pip install -r requirements.txt
    ```

---

## ⚙️ Cara Menjalankan

Ikuti langkah-langkah berikut secara berurutan:

1.  **Jalankan Preprocessing Data**
    Perintah ini akan membersihkan data mentah dan menyimpan hasilnya beserta *vectorizer*.
    ```bash
    python preprocessing/automate_crypto_preprocessing.py \
      --input data/crypto_news_raw.csv \
      --output data/crypto_news_clean.csv \
      --vectorizer artifacts/vectorizer.pkl
    ```

2.  **Latih dan Lacak Model dengan MLflow**
    Masuk ke direktori model dan jalankan pipeline MLflow.
    ```bash
    cd Membangun_model
    mlflow run . -P data_path=../data/crypto_news_clean.csv
    ```
    *Untuk melihat hasilnya, jalankan `mlflow ui` di terminal.*

3.  **Jalankan Layanan API**
    Pilih salah satu framework untuk menjalankan server.

    ```bash
    # Opsi 1: Menggunakan Flask
    flask run --port 5000

    # Opsi 2: Menggunakan FastAPI
    uvicorn app:app --reload --port 8000
    ```

4.  **Uji Coba Endpoint Prediksi**
    Kirim permintaan ke API menggunakan skrip inferensi.
    ```bash
    python inference.py --text "Bitcoin surges after ETF approval"
    ```

---

## 📊 Performa Model

Metrik berikut dicatat pada *run* terbaik di MLflow.

| Metrik          | Skor    |
| --------------- | ------- |
| **Accuracy**    | `0.829` |
| **Precision**   | `0.846` |
| **Recall**      | `0.829` |
| **ROC AUC**     | `0.905` |
| **F1 Score**    | `0.828` |
| **Waktu Latih** | `83.17s`|

---

## 🆘 Bantuan (Troubleshooting)

-   **Error `NLTK data missing`:**
    Jalankan perintah Python berikut untuk mengunduh data yang dibutuhkan.
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    ```

-   **MLflow UI tidak menampilkan *runs*:**
    Pastikan Anda menjalankan UI dari direktori root proyek.
    ```bash
    mlflow ui --backend-store-uri ./mlruns
    ```

-   **Melihat opsi untuk skrip:**
    Gunakan flag `--help` untuk melihat argumen yang tersedia.
    ```bash
    python app.py --help
    ```

---

## ✍️ Penulis

-   **De Mahesta** – [dewamahesta2711@gmail.com](mailto:dewamahesta2711@gmail.com) | 

---

## 📜 Riwayat Versi

-   **v0.2**
    -   Menambahkan CI/CD dengan GitHub Actions.
    -   Mengintegrasikan monitoring & alerting dengan Prometheus/Grafana.
-   **v0.1**
    -   Rilis awal: preprocessing, pemodelan, dan serving API.

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Lihat file [LICENSE.md](LICENSE.md) untuk detailnya.

---

## 🙏 Ucapan Terima Kasih

-   Dataset [Crypto News +](https://www.kaggle.com/datasets/oliviervha/crypto-news)
-   Contoh penggunaan [TextBlob](https://textblob.readthedocs.io/en/dev/)
-   Snippets alur kerja oleh [PurpleBooth](https://github.com/PurpleBooth)
-   Dokumentasi MLflow oleh [dbader](https://github.com/dbader)
-   Pola desain Grafana oleh [zenorocha](https://github.com/zenorocha)
