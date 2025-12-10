# Kubernetes LEMP Stack Application
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Nginx](https://img.shields.io/badge/Nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

This project demonstrates a **multi-container LEMP-style application** running on **Kubernetes (Minikube)**.  
The application is exposed publicly through a **host Nginx reverse proxy** under the path `/kube`.

## Architecture

The application consists of three main components, each running in its own Kubernetes Deployment:

- **Frontend**: Nginx  
- **Backend**: Python (Flask) REST API  
- **Database**: MySQL with persistent storage

All components communicate using Kubernetes Services and internal DNS.
```
Internet
|
Host Nginx (Reverse Proxy)
|
└── /kube
|
Minikube NodePort
|
Frontend (Nginx)
|
Backend (Flask API)
|
MySQL (PVC)
```
---

## Features

- Kubernetes-based multi-container application
- Reverse proxy routing via Nginx (`/kube`)
- Persistent MySQL storage using PersistentVolumeClaim
- REST API implemented with Flask
- Frontend UI served by Nginx
- Database operations fully handled inside Kubernetes

### UI Features
- **Health check** (`/api/health`)
- **Initialize database** (`/api/init-db`)
- **List users** (`/api/users`)
- **Delete all users** (`/api/delete-users`)
- Basic CSS styling for improved usability

---

## Technologies Used

- Kubernetes (Minikube)
- Docker
- Nginx
- Python 3.11 / Flask
- MySQL 8.0
- GitHub (version control)<br>
![Kubernetes](https://img.shields.io/badge/Kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-%23663399.svg?style=for-the-badge&logo=css&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
---

## Repository Structure
```
.
├── backend
│ ├── app.py
│ ├── Dockerfile
│ └── requirements.txt
├── frontend
│ ├── Dockerfile
│ ├── index.html
│ ├── nginx.conf
│ └── style.css
├── k8s
│ ├── backend-configmap.yaml
│ ├── backend-deployment.yaml
│ ├── frontend-deployment.yaml
│ └── mysql
│ ├── mysql-deployment.yaml
│ ├── mysql-pvc.yaml
│ └── mysql-secret.yaml
└── .gitignore
```
⚠️ **Secrets Note**  
Actual database passwords are not pushed to the public repository.  
Secrets should be created manually in the cluster using environment-specific values.

---

## Deployment Overview

1. Minikube is used as the Kubernetes cluster.
2. Docker images are built inside the Minikube Docker environment.
3. Kubernetes manifests are applied using `kubectl`.
4. Frontend is exposed via a NodePort Service.
5. Host Nginx proxies `/kube` traffic to Minikube.
6. Backend communicates with MySQL using Kubernetes DNS (`mysql` service).

The application continues to run independently of SSH sessions.

---

## Example Endpoints

- UI:  
```
http://<SERVER-IP>/kube
```
- API (through frontend proxy):  
```
/kube/api/health
/kube/api/init-db
/kube/api/users
/kube/api/delete-users
```
---

## Persistence

- MySQL data is stored using a Kubernetes PersistentVolumeClaim.
- Data remains intact even if pods are restarted.

---

## Educational Goals

This project demonstrates:

- Kubernetes deployments, services, config maps, secrets, and volumes
- Container-to-container communication in Kubernetes
- Reverse proxying traffic to a Kubernetes cluster
- Practical use of Kubernetes for a multi-service application

---

## Status

✅ Application running  
✅ Kubernetes orchestration used  
✅ Database persistence enabled  
✅ Publicly accessible through reverse proxy  

---
