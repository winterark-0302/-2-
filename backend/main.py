from fastapi import FastAPI, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI(title="SafeK Backend API", version="1.0.0")

# Prometheus Metrics
REQUEST_COUNT = Counter("api_requests_total", "Total API Requests", ["method", "endpoint"])

@app.get("/")
def read_root():
    REQUEST_COUNT.labels(method="GET", endpoint="/").inc()
    return {"status": "ok", "message": "SafeK API is running"}

@app.get("/metrics")
def metrics():
    """Expose metrics for Prometheus scraping"""
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/api/health")
def health_check():
    REQUEST_COUNT.labels(method="GET", endpoint="/api/health").inc()
    return {"status": "healthy", "service": "SafeK Summer MVP"}
