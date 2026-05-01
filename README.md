# Real-Time Anomaly Detection System

## 🚀 Overview

This project implements a real-time anomaly detection system for streaming time-series data.
It combines statistical methods, machine learning models, and production-style system design to detect unusual patterns in data streams such as system metrics, financial data, or logs.

The goal is to bridge the gap between **machine learning models** and **production systems**.

---

## 🎯 Problem Statement

Modern systems generate continuous streams of data (CPU usage, transactions, logs).
Detecting anomalies in real time is critical for:

* System reliability (incident detection)
* Fraud detection
* Monitoring and alerting

This project explores:

* How to detect anomalies in streaming data
* Trade-offs between simple statistical methods and ML models
* How to deploy ML models in a real-time system

---

## 🏗️ System Architecture

```
                +------------------+
                |   Data Source    |
                | (Simulated/Real) |
                +--------+---------+
                         |
                         v
                +------------------+
                | Streaming Layer  |
                | (Generator/Kafka)|
                +--------+---------+
                         |
                         v
                +----------------------+
                | Feature Engineering  |
                | - Rolling Mean       |
                | - Rolling Std Dev    |
                | - Z-score            |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |   Model Layer        |
                |----------------------|
                | 1. Z-score           |
                | 2. Isolation Forest  |
                | 3. Autoencoder       |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |  Anomaly Detection   |
                |  (Thresholding)      |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Alerting & API Layer |
                | (FastAPI)            |
                +----------+-----------+
                           |
                           v
                +----------------------+
                | Visualization Layer  |
                | (Dashboard/Plots)    |
                +----------------------+
```

---

## ⚙️ Tech Stack

* Python
* NumPy / Pandas
* Scikit-learn
* PyTorch (for autoencoder)
* FastAPI (serving layer)
* Matplotlib / Plotly (visualization)

---

## 🧪 Models Implemented

### 1. Statistical Baseline (Z-score)

* Detects anomalies based on deviation from mean
* Fast and interpretable
* Weak for complex patterns

### 2. Isolation Forest

* Tree-based anomaly detection
* Works well for high-dimensional data
* Less interpretable

### 3. Autoencoder (Neural Network)

* Learns normal patterns
* Detects anomalies via reconstruction error
* More powerful but requires tuning

---

## 📊 Evaluation Strategy

* Compare models on:

  * Precision / Recall
  * False positive rate
  * Detection latency
* Analyze trade-offs:

  * Accuracy vs interpretability
  * Performance vs complexity

---

## 🚦 API Endpoints (Planned)

* `POST /predict` → detect anomaly for input data
* `GET /stream` → simulate real-time data stream
* `GET /metrics` → system + model metrics

---

## 📁 Project Structure

```
ml-anomaly-detection/
│
├── data/               # datasets / synthetic data
├── features/           # feature engineering logic
├── models/             # ML models
├── streaming/          # streaming simulation / Kafka
├── api/                # FastAPI service
├── visualization/      # plots / dashboards
├── tests/              # unit tests
└── README.md
```

---

## 🔍 Key Learnings (Goals)

* Understand anomaly detection techniques deeply
* Learn trade-offs between statistical vs ML approaches
* Build production-ready ML systems
* Handle streaming and real-time constraints

---

## 🛠️ Future Improvements

* Kafka-based real-time streaming
* Concept drift detection
* Feedback loop for false positives
* Model retraining pipeline

---

## ▶️ How to Run (TBD)

Instructions will be added as components are implemented.

---

## 💡 Motivation

Most ML projects stop at notebooks.
This project focuses on **end-to-end system design**, from data ingestion to model serving and monitoring.

---
