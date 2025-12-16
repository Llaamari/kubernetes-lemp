# Kubernetes LEMP Stack with CI/CD Frontend

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326ce5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-0db7ed?style=for-the-badge&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

This project demonstrates a **multi-container LEMP-style application running on Kubernetes (Minikube)**, extended with a **CI/CD-enabled frontend** exposed under `/cicd`.

The application is publicly accessible through a **host-level Nginx reverse proxy**, while all services run inside Kubernetes.

---

## Architecture Overview

The system consists of **two frontends**, **two backends**, and **one database**, all orchestrated with Kubernetes.
```
Internet
|
Host Nginx (Reverse Proxy)
|
├── /kube → Original application
│ └── Frontend (Nginx)
│ └── Backend (Flask)
│ └── MySQL (PVC)
|
└── /cicd → CI/CD-enabled application
└── Frontend-CICD (Nginx)
└── Backend-CICD (Flask)
└── MySQL (PVC)
```

---

## Features

### Core Kubernetes Features
- Multi-container application using Kubernetes Deployments and Services
- Internal service discovery via Kubernetes DNS
- Persistent MySQL storage using PersistentVolumeClaim
- Configuration handled with ConfigMaps and Secrets
- Independent frontend and backend scaling

### Application Features
- REST API built with Flask
- Frontend served by Nginx
- Reverse proxy routing via host Nginx
- CSS-styled user interface

### UI Functionality
The frontend provides buttons for:
- **Health check** (`/api/health`)
- **Initialize database** (`/api/init-db`)
- **List users** (`/api/users`)
- **Add user** (`/api/add-user`)
- **Delete all users** (`/api/delete-users`)

All operations persist data in a Kubernetes-managed MySQL database.

---

## CI/CD Implementation

This project includes a **GitHub Actions CI pipeline**:

- Docker image build for the CICD frontend
- Workflow triggered on `push` to `main`
- Executed using a **self-hosted GitHub Actions runner** on the VPS
- Ensures builds and validations occur in the same environment as Kubernetes

> A self-hosted runner is required because GitHub-hosted runners cannot access a private Minikube cluster.

---

## Repository Structure
```
├── backend
│ ├── app.py
│ ├── Dockerfile
│ └── requirements.txt
├── backend-cicd
│ ├── app.py
│ ├── Dockerfile
│ └── requirements.txt
├── frontend
│ ├── Dockerfile
│ ├── index.html
│ ├── nginx.conf
│ └── style.css
├── frontend-cicd
│ ├── Dockerfile
│ ├── index.html
│ ├── nginx.conf
│ └── style.css
├── k8s
│ ├── backend-configmap.yaml
│ ├── backend-deployment.yaml
│ ├── backend-cicd-deployment.yaml
│ ├── frontend-deployment.yaml
│ ├── frontend-cicd-deployment.yaml
│ └── mysql
│ ├── mysql-deployment.yaml
│ ├── mysql-pvc.yaml
│ └── mysql-secret.yaml
├── .github
│ └── workflows
│ └── cicd-deploy.yml
└── .gitignore
```
---

## Secrets Handling

⚠️ **Security Notice**

Sensitive values such as database passwords are **not committed to the repository**.

- Secrets are managed using Kubernetes `Secret` objects
- `.gitignore` explicitly excludes secret files
- GitHub Secrets are used for CI/CD configuration

---

## Deployment Summary

1. Minikube runs on a VPS as the Kubernetes cluster
2. Docker images are built inside Minikube’s Docker environment
3. Kubernetes manifests are applied with `kubectl`
4. Frontends are exposed via NodePort services
5. Host Nginx routes traffic:
   - `/kube` → original application
   - `/cicd` → CI/CD-enabled application
6. Services continue running independently of SSH sessions

---

## Access URLs

- **Original application**
```
http://86.50.21.122/kube/
```
- **CI/CD application**
```
http://86.50.21.122/cicd/
```
- **API examples**
```
/cicd/api/health
/cicd/api/init-db
/cicd/api/users
/cicd/api/add-user
/cicd/api/delete-users
```
---

## Persistence

- MySQL uses a PersistentVolumeClaim
- Database data survives pod restarts and redeployments

---

## Educational Goals

This project demonstrates:

- Kubernetes application architecture
- Multi-service communication in Kubernetes
- Reverse proxying to Kubernetes from a host server
- Practical CI/CD with GitHub Actions
- Secure secret handling
- Self-hosted GitHub Actions runners

---

## Status

✅ Kubernetes orchestration in use  
✅ CI/CD pipeline implemented  
✅ Persistent database storage  
✅ Public access via reverse proxy  
✅ UI + API fully functional  

---
