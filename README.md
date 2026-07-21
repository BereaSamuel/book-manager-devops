# 📚 Book Manager - DevOps Project

## Project Overview

Book Manager is a web application developed using **Python** and **Flask** for managing a collection of books.

The application allows users to add, edit, delete and view books stored in a **SQLite** database.

This project demonstrates the implementation of a complete DevOps workflow, including:

- Source Control using Git and GitHub
- Docker Containerization
- Continuous Integration & Continuous Deployment with Jenkins
- Kubernetes Deployment using Minikube
- Monitoring with Prometheus and Grafana
- Application Logging
- Automated Testing

---

# Project Architecture

```
Developer
    │
    ▼
GitHub Repository
    │
    ▼
Jenkins CI/CD Pipeline
    │
    ├── Checkout Source Code
    ├── Install Dependencies
    ├── Run Unit Tests
    ├── Build Docker Image
    ├── Deploy Docker Container
    ▼
Docker
    │
    ▼
Kubernetes (Minikube)
    │
    ▼
Prometheus
    │
    ▼
Grafana Dashboard
```

---

# Project Status

✅ Project Completed

All requested DevOps components have been successfully implemented and validated.

---

# Technologies Used

## Backend

- Python 3
- Flask

## Frontend

- HTML5
- CSS3

## Database

- SQLite

## DevOps Tools

- Git
- GitHub
- Docker
- Jenkins
- Kubernetes
- Minikube
- Helm
- Prometheus
- Grafana

---

# Application Features

The application provides the following functionality:

- Add new books
- View all books
- Edit existing books
- Delete books
- Automatic SQLite database initialization
- Persistent data storage using Docker Volumes
- Automated testing
- Docker container deployment
- Kubernetes deployment
- Monitoring with Prometheus
- Custom Grafana Dashboard
- Kubernetes application logging
- Automated Jenkins Pipeline

---

# Project Structure

```
book-manager/
│
├── app.py
├── init_db.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── README.md
├── .gitignore
├── .dockerignore
│
├── kubernetes/
│   ├── deployment.yaml
│   └── service.yaml
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── edit.html
│
└── Screenshots/
```

---

# Database

The application uses a lightweight **SQLite** database.

Database file:

```
books.db
```

Table:

```
books
```

Columns:

- id
- title
- author

The database is automatically created during the first application startup if it does not already exist.

---

# Installation

Clone the repository

```bash
git clone https://github.com/BereaSamuel/book-manager-devops.git

cd book-manager-devops
```

Install dependencies

```bash
pip3 install -r requirements.txt
```

Run the application

```bash
python3 app.py
```

Application URL

```
http://localhost:5000
```

---

# Docker Containerization

Build the Docker image

```bash
docker build -t book-manager:1.0 .
```

Run the container

```bash
docker run -d \
--name book-manager-container \
-p 5000:5000 \
-v book-manager-data:/app/data \
-e DATABASE_PATH=/app/data/books.db \
book-manager:1.0
```

Verify the running container

```bash
docker ps
```

The SQLite database is stored inside a Docker Volume, ensuring that all data remains available even after restarting the container.

---

# Jenkins CI/CD Pipeline

The Jenkins pipeline performs the following stages automatically:

1. Checkout Source Code
2. Install Python Dependencies
3. Execute Automated Tests
4. Build Docker Image
5. Stop Previous Container
6. Deploy Updated Container
7. Verify Successful Deployment

If any automated test fails, deployment is immediately stopped.

---

# Automated Testing

The project uses Python's built-in **unittest** framework.

Implemented tests verify:

- Homepage availability
- Book creation
- HTTP response validation

Run tests manually

```bash
python3 -m unittest test_app.py
```

---

# Kubernetes Deployment

The application is deployed inside a local Kubernetes cluster using **Minikube**.

Deployment resources include:

- Deployment
- NodePort Service

Deploy the application

```bash
kubectl apply -f kubernetes/
```

Verify deployment

```bash
kubectl get deployments

kubectl get pods

kubectl get services
```

Open the application

```bash
minikube service book-manager-service
```

The application is exposed through a Kubernetes NodePort Service.

---

# Monitoring

Monitoring is implemented using the **kube-prometheus-stack** Helm chart.

Installed monitoring components:

- Prometheus
- Grafana
- Alertmanager
- kube-state-metrics
- Node Exporter

Installation

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

helm repo update

helm install monitoring prometheus-community/kube-prometheus-stack
```

Prometheus continuously collects metrics from the Kubernetes cluster and running containers.

---

# Grafana Dashboard

A custom Grafana dashboard was created specifically for monitoring the Book Manager application.

Dashboard panels include:

- CPU Usage
- Working Memory Usage
- Total CPU Time
- RSS Memory Usage

The dashboard refreshes automatically every 10 seconds using metrics collected by Prometheus.

---

# Application Logging

Application logs are collected directly from the running Kubernetes Pod.

View logs

```bash
kubectl logs deployment/book-manager
```

View resource usage

```bash
kubectl top pods

kubectl top nodes
```

Logs include incoming HTTP requests, application events and Kubernetes runtime information.

---

# DevOps Workflow

```
Developer
      │
      ▼
GitHub Repository
      │
      ▼
Jenkins Pipeline
      │
      ▼
Docker Image
      │
      ▼
Kubernetes Deployment
      │
      ▼
Prometheus Monitoring
      │
      ▼
Grafana Dashboard
```

---

# Project Results

This project successfully demonstrates:

- Source Control using Git and GitHub
- Automated CI/CD Pipeline
- Docker Containerization
- Persistent Data Storage
- Kubernetes Deployment
- Prometheus Monitoring
- Grafana Visualization
- Kubernetes Logging
- Automated Unit Testing

---

# Screenshots

The **Screenshots** directory contains images illustrating every major stage of the project:

- Flask Web Application
- Docker Container
- Jenkins Build
- Jenkins Pipeline Execution
- Kubernetes Deployment
- Kubernetes Pods and Services
- Prometheus Monitoring
- Grafana Dashboard
- Kubernetes Application Logs

---

# Future Improvements

Possible future enhancements include:

- Jenkins deployment directly to Kubernetes
- Docker Hub image publishing
- GitHub Webhooks
- HTTPS with Kubernetes Ingress
- Horizontal Pod Autoscaler
- Multiple application replicas
- Prometheus application metrics using `prometheus_client`

---

# Author

**Samuel Berea**

GitHub:

https://github.com/BereaSamuel