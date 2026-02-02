## 🚀 Getting Started
### 1. How to clone the repository
```bash
git clone https://github.com/liron-dev/cars.git
cd cars
```
### 2. Operate locally with docker compose
```bash
# first command to start, second command to stop:
docker-compose up -d --build web
docker-compose down --volumes --rmi local --remove-orphans
# flags are optional and will DELETE APP IMAGE AND VOLUMES
```
### 3. Operate with minikube
```bash
minikube start --driver=docker --nodes 2
docker build -t car-app-web:latest ./app
minikube image load car-app-web:latest
kubectl apply -k .
# remove objects:
kubectl delete -k . --ignore-not-found
# delete minikube:
minikube delete 
```
## 📊 Observability & Monitoring

This stack includes a full monitoring pipeline to track application health and database performance:

* **Prometheus**: Our time-series database and monitoring tool. It "scrapes" (pulls) metrics from the Web App and the Postgres Exporter at regular intervals.
* **Grafana**: The visualization layer. It connects to Prometheus as a data source to turn raw numbers into beautiful, actionable dashboards.
* **Postgres Exporter**: A "sidecar" service that logs into PostgreSQL, gathers internal performance stats (like active connections or query rates), and exposes them for Prometheus to read.
* **Prometheus Flask Exporter**: Integrated directly into the Python code to provide request rates, latency, and error counts.
