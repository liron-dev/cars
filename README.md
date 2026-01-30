## 🚀 Getting Started

### 1. How to clone the repository
```bash
git clone https://github.com/liron-dev/cars.git

---

## 📊 Observability & Monitoring

This stack includes a full monitoring pipeline to track application health and database performance:

* **Prometheus**: Our time-series database and monitoring tool. It "scrapes" (pulls) metrics from the Web App and the Postgres Exporter at regular intervals.
* **Grafana**: The visualization layer. It connects to Prometheus as a data source to turn raw numbers into beautiful, actionable dashboards.
* **Postgres Exporter**: A "sidecar" service that logs into PostgreSQL, gathers internal performance stats (like active connections or query rates), and exposes them for Prometheus to read.
* **Prometheus Flask Exporter**: Integrated directly into the Python code to provide request rates, latency, and error counts.
