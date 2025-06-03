from prometheus_client import start_http_server, Counter, Histogram
from flask import Flask
import random
import time
import threading

# Definisikan metrik
model_predictions = Counter(
    'model_prediction_total',
    'Jumlah prediksi yang dilakukan oleh model',
    labelnames=['sentiment']
)

model_errors = Counter(
    'model_prediction_errors_total',
    'Jumlah error saat melakukan prediksi'
)

response_time = Histogram(
    'model_response_time_seconds',
    'Waktu respon model per prediksi'
)

cpu_usage = Histogram(
    'system_cpu_usage_percent',
    'Penggunaan CPU (%)'
)

memory_usage = Histogram(
    'system_memory_usage_percent',
    'Penggunaan Memory (%)
)

disk_usage = Histogram(
    'system_disk_usage_percent',
    'Penggunaan Disk (%)
)

http_requests = Counter(
    'http_request_total',
    'Jumlah HTTP request',
    labelnames=['endpoint', 'method']
)

error_rate = Histogram(
    'model_error_rate',
    'Error rate simulasi (untuk demo)'
)

@app.before_request
def before_request():
    http_requests.labels(endpoint=request.path, method=request.method).inc()

@response_time.time()
def record_response_time():
    return random.uniform(0.01, 0.5)

# Simulasi metrik tambahan
def simulate_metrics():
    while True:
        cpu_usage.observe(random.uniform(10, 90))
        memory_usage.observe(random.uniform(20, 85))
        disk_usage.observe(random.uniform(30, 95))
        error_rate.observe(random.uniform(0, 1))
        time.sleep(1)

# Jalankan server Flask + metrik Prometheus
app = Flask(__name__)
start_http_server(8000)

threading.Thread(target=simulate_metrics, daemon=True).start()

@app.route("/predict", methods=["POST"])
def predict():
    record_response_time()
    sentiment = random.choice(['Negative', 'Neutral', 'Positive'])
    model_predictions.labels(sentiment=sentiment).inc()
    return jsonify({"sentiment": sentiment})

if __name__ == "__main__":
    app.run(port=5000)