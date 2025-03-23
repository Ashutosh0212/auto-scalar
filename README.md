# Auto-Scaling Local VM to GCP Project

## Objective
Monitor local VM resource usage using Prometheus and trigger an auto-scaling mechanism that launches a GCP VM when CPU usage exceeds 75%.

## Components
- Prometheus + Node Exporter
- Python Auto-Scaler Script
- GCP VM with Flask App deployed via `startup.sh`

## Setup
1. Configure Prometheus with `prometheus.yml`.
2. Run `auto_scaler.py` in the local VM.
3. Simulate high CPU load using a tool like `stress`.
4. The Auto-Scaler will create a new GCP VM running a Flask application.

## Authors
- Ashutosh
