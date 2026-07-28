# 📚 Book Manager - DevOps Project

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Jenkins](https://img.shields.io/badge/Jenkins-CI/CD-red)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Minikube-326CE5)
![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-orange)
![Grafana](https://img.shields.io/badge/Dashboard-Grafana-F46800)
![MySQL](https://img.shields.io/badge/Database-MySQL-4479A1)

---

# 📖 Project Overview

**Book Manager** is a web application developed using **Python** and **Flask** for managing a collection of books.

The application provides complete CRUD functionality (Create, Read, Update and Delete) while storing data inside a **MySQL** database running in a Docker container.

The purpose of this project is to demonstrate a complete DevOps workflow including:

- Git & GitHub Source Control
- Docker Containerization
- Continuous Integration / Continuous Deployment with Jenkins
- Kubernetes Deployment using Minikube
- Monitoring with Prometheus
- Visualization with Grafana
- Kubernetes Logging
- Automated Testing

---

# 🏗 Project Architecture

```
                 Developer
                     │
                     ▼
              GitHub Repository
                     │
                     ▼
            Jenkins CI/CD Pipeline
                     │
     ┌───────────────┼────────────────┐
     │               │                │
 Checkout        Unit Tests      Docker Build
     │               │                │
     └───────────────┴────────────────┘
                     │
                     ▼
              Docker Container
                     │
                     ▼
            Kubernetes (Minikube)
                     │
          ┌──────────┴──────────┐
          │                     │
     Prometheus            Grafana
          │                     │
          └──────── Monitoring ─┘
                     │
                     ▼
                  MySQL
```

---

# ✅ Project Features

The application provides:

- Add new books
- View all books
- Edit existing books
- Delete books
- Persistent MySQL database
- Docker container deployment
- Jenkins CI/CD Pipeline
- Kubernetes Deployment
- Prometheus Monitoring
- Grafana Dashboard
- Kubernetes Logging
- Automated Unit Testing

---

# 🛠 Technologies Used

## Backend

- Python 3.10
- Flask

## Frontend

- HTML5
- CSS3

## Database

- MySQL 8.0

## DevOps

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

# 📂 Project Structure

```
book-manager/
│
├── app.py
├── requirements.txt
├── test_app.py
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
    ├── webapp.png
    ├── mysql.png
    ├── docker.png
    ├── jenkins-build.png
    ├── jenkins-pipeline.png
    ├── jenkins-pipeline2.png
    ├── kubernetes-app.png
    ├── kubernetes-pods.png
    ├── kubectl-logs.png
    ├── prometheus-targets.png
    └── grafana-dash.png
```

---

# 🗄 Database

The application uses **MySQL 8.0** running inside a Docker container.

Database:

```
book_manager
```

Table:

```
books
```

Columns

- id
- title
- author

Connection is configured using environment variables:

```
DB_HOST
DB_PORT
DB_NAME
DB_USER
DB_PASSWORD
```

---

# ⚙ Installation

Clone repository

```bash
git clone https://github.com/BereaSamuel/book-manager-devops.git

cd book-manager-devops
```

Install dependencies

```bash
pip3 install -r requirements.txt
```

Start MySQL

```bash
docker start mysql-bookmanager
```

Run Flask

```bash
python3 app.py
```

Application

```
http://localhost:5000
```

---

# 🐳 Docker

Build image

```bash
docker build -t book-manager:2.0 .
```

Run container

```bash
docker run -d \
--name book-manager-container \
-p 5001:5000 \
--add-host=host.docker.internal:host-gateway \
-e DB_HOST=host.docker.internal \
-e DB_PORT=3306 \
-e DB_NAME=book_manager \
-e DB_USER=bookuser \
-e DB_PASSWORD=bookpass \
book-manager:2.0
```

Verify

```bash
docker ps
```

Docker application

```
http://localhost:5001
```

---

# 🔄 Jenkins CI/CD

The Jenkins pipeline performs the following stages automatically:

1. Checkout source code
2. Install dependencies
3. Run automated tests
4. Build Docker image
5. Stop previous container
6. Deploy updated container
7. Verify successful deployment

If any test fails, deployment is automatically stopped.

Jenkins

```
http://localhost:8080
```

Pipeline deployment

```
http://localhost:5002
```

---

# 🧪 Automated Testing

The project uses Python's built-in **unittest** framework.

Run tests manually

```bash
python3 -m unittest test_app.py
```

Implemented tests:

- Homepage availability
- Book creation
- HTTP response validation

---

# ☸ Kubernetes

Start Minikube

```bash
minikube start
```

Deploy

```bash
kubectl apply -f kubernetes/
```

Verify deployment

```bash
kubectl get deployments

kubectl get pods

kubectl get services
```

Open application

```bash
minikube service book-manager-service
```

---

# 📊 Monitoring

Monitoring is implemented using the **kube-prometheus-stack** Helm chart.

Installed components

- Prometheus
- Grafana
- Alertmanager
- kube-state-metrics
- Node Exporter

Access Prometheus

```bash
kubectl port-forward svc/monitoring-kube-prometheus-prometheus 9090:9090
```

Open

```
http://localhost:9090
```

---

# 📈 Grafana

Start Grafana

```bash
kubectl port-forward svc/monitoring-grafana 3000:80
```

Open

```
http://localhost:3000
```

The custom dashboard monitors:

- CPU Usage
- Working Memory Usage
- Total CPU Time
- RSS Memory

Dashboard refresh interval:

```
10 seconds
```

---

# 📋 Kubernetes Logging

View logs

```bash
kubectl logs deployment/book-manager
```

Resource usage

```bash
kubectl top pods

kubectl top nodes
```

---

# 🚀 DevOps Workflow

```
Developer
     │
     ▼
GitHub
     │
     ▼
Jenkins Pipeline
     │
     ▼
Docker
     │
     ▼
Kubernetes
     │
     ▼
Prometheus
     │
     ▼
Grafana
     │
     ▼
MySQL
```

---

# 📷 Screenshots

The repository includes screenshots for every major stage of the project:

- Web Application
- MySQL Database
- Docker Container
- Jenkins Build
- Jenkins Pipeline
- Kubernetes Application
- Kubernetes Pods
- Prometheus Targets
- Grafana Dashboard
- Kubernetes Logs

---

# 🚀 Future Improvements

Possible future improvements:

- Deploy directly to Kubernetes from Jenkins
- Publish Docker images to Docker Hub
- Configure GitHub Webhooks
- HTTPS using Kubernetes Ingress
- Horizontal Pod Autoscaler (HPA)
- Multiple application replicas
- Deploy on a cloud Kubernetes platform (EKS, AKS or GKE)

---

# 👨‍💻 Author

**Samuel Berea**

GitHub:

https://github.com/BereaSamuel/book-manager-devops