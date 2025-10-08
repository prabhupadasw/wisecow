# Wisecow DevOps Assignment - Accuknox

## Overview
This project containerizes and deploys the Wisecow application on Kubernetes with secure HTTPS/TLS communication.

## Features Implemented
- ✅ **Dockerization**: Custom Dockerfile for Wisecow app
- ✅ **Kubernetes Deployment**: Complete K8s manifests (Deployment, Service, Ingress)
- ✅ **CI/CD Pipeline**: GitHub Actions for automated Docker image builds
- ✅ **HTTPS/TLS**: Secure communication using NGINX Ingress with TLS certificates
- ✅ **Container Registry**: Docker Hub integration

## Architecture
- **Container**: Docker image with Wisecow app and dependencies
- **Orchestration**: Kubernetes (Docker Desktop)
- **Load Balancer**: NGINX Ingress Controller
- **Security**: TLS/SSL termination with self-signed certificates

## Files Structure
├── Dockerfile # Container image definition
├── wisecow-deployment.yaml # K8s Deployment and Service
├── wisecow-ingress.yaml # HTTPS Ingress configuration
├── .github/workflows/ # CI/CD pipeline
└── README.md # This file


## Deployment Instructions

### Prerequisites
- Docker Desktop with Kubernetes enabled
- kubectl configured
- NGINX Ingress Controller installed

### Steps
1. **Build and Deploy:**
kubectl apply -f wisecow-deployment.yaml
kubectl apply -f wisecow-ingress.yaml

2. **Generate TLS Certificate:**
openssl req -x509 -newkey rsa:4096 -keyout tls.key -out tls.crt -days 365 -nodes -subj "/CN=wisecow.local"
kubectl create secret tls wisecow-tls --cert=tls.crt --key=tls.key

3. **Update hosts file:**
Add `127.0.0.1 wisecow.local` to `/etc/hosts` (Linux/Mac) or `C:\Windows\System32\drivers\etc\hosts` (Windows)

4. **Access Application:**
- HTTP: http://localhost:31269
- HTTPS: https://wisecow.local

## CI/CD Pipeline
GitHub Actions automatically builds and pushes Docker images to Docker Hub on every commit to main branch.

## Security
- TLS encryption for all communication
- Self-signed certificates for local development
- Container runs as non-root user

## Author
Prabhupada Swain - DevOps Trainee Assessment








## Problem Statement 2: 

ps2-devops-scripts/README.md
System Health Monitoring Script (health_monitor.py)
Description:
A Python script that continuously monitors CPU usage, memory usage, disk space, and running process count on a Linux/Windows system.

If CPU > 80%, Memory > 80%, or Disk > 90%, it prints an alert and logs it to health_alerts.log.

Runs checks every 10 seconds (configurable).
Install dependencies:
pip install psutil
Run the script:
python health_monitor.py
Stop: Press Ctrl+C to stop monitoring.

Output:

Shows system stats in your terminal.

Logs all alerts with timestamps to health_alerts.log (in the same folder).

Sample alert (in health_alerts.log):
Tue Oct  7 22:37:14 2025: Memory usage high!

##(ii)Application Health Checker (app_health_checker.py)

A Python script that checks whether web applications are "UP" (HTTP 200) or "DOWN" (other status code or error) and logs the results.
Install required package:
pip install requests

Run the script:
python app_health_checker.py

Check app_health.log for timestamped uptime/downtime status.
https://wisecow.local is DOWN (error: certificate verify failed...)
https://google.com is UP (status: 200)
https://github.com is UP (status: 200)
Results are also saved to app_health.log in the same folder.

After adding, commit and push:
git add README.md
git commit -m "Update README: add application health checker instructions"
git push origin main






## Problem Statement 3 (Optional): KubeArmor Security Policy

Although Problem Statement 3 is optional, I attempted to implement a KubeArmor file access blocking policy for the Wisecow application.

### Steps performed:
- Installed KubeArmor in Kubernetes cluster.
- Created a security policy (`deny-one-file.yaml`) to block `/tmp/forbidden.txt`.
- Applied the policy and restarted pods.
- Tested file creation inside pod and checked `karmor logs`.
- Found that the policy was applied to the pod but blocking did not occur (no alerts). Pod label matched policy selector.

### Files included:
- `deny-one-file.yaml` — policy definition.

### Result:
- No KubeArmor block was triggered for file creation. Work is documented as attempted; will troubleshoot further in future.




