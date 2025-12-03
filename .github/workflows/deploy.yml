```text
  █████         █████████   ███████████     ██████████
▒▒███         ███▒▒▒▒▒███ ▒▒███▒▒▒▒▒███   ▒███▒▒▒▒▒▒█
 ▒███        ▒███    ▒███  ▒███    ▒███   ▒███     ▒ 
 ▒███        ▒███████████  ▒██████████    ▒█████████ 
 ▒███        ▒███▒▒▒▒▒███  ▒███▒▒▒▒▒███   ▒▒▒▒▒▒▒▒███
 ▒███      █ ▒███    ▒███  ▒███    ▒███    ███   ▒███
 ███████████ █████   █████ ███████████    ▒▒████████ 
▒▒▒▒▒▒▒▒▒▒▒ ▒▒▒▒▒   ▒▒▒▒▒ ▒▒▒▒▒▒▒▒▒▒▒      ▒▒▒▒▒▒▒▒  
```

# MLOps Lab 5: Automation with GitHub Actions

**Course:** MLOps - AIVANCITY 2025-2026  
**Authors:** Jeremie ONDZAGHE & Dylan ONDO

[![Docker Image](https://img.shields.io/docker/pulls/dockerjeremieo1/hello_world.svg)](https://hub.docker.com/r/dockerjeremieo1/hello_world)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automated-blue)](https://github.com/Blurenis/MLops_Lab_5/actions)

## 📖 Introduction

The objective of this lab was to implement a complete **Continuous Integration and Continuous Deployment (CI/CD)** pipeline for a simple Flask application. We used **GitHub Actions** to automate testing (Linter, Unittests) and deployment (Build & Push to Docker Hub).

This work was carried out collaboratively, simulating a real-world workflow with branch management and Pull Requests.

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Docker (optional, for local container testing)

### Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/Blurenis/MLops_Lab_5.git
cd MLops_Lab_5
pip install -r requirements.txt
```

### Running Locally

To run the Flask application on your local machine:

```bash
python hello_world.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

> **Note:** Accessing the root `/` may return a 404. Use the `/greeting` route to see the app in action.

### Running Tests

To launch the unit tests locally:

```bash
pytest test_hello_world.py
```

## 🛠 CI/CD Pipeline

We have configured **GitHub Actions** to handle the automation. The workflows are located in `.github/workflows/`.

### 1. Quality & Testing
Triggered on `push` and `pull_request` to `main`.
- **Linter (`linter.yml`):** Checks code syntax and style compliance using Flake8.
- **Unit Tests (`test.yml`):** Automatically runs the test suite (`unittest`/`pytest`) to ensure code stability.

### 2. Deployment (`deploy.yml`)
Triggered on `push` to `main`.
This workflow performs the following steps:
1.  **Build Binary:** Compiles the Python script into an executable using **PyInstaller**.
2.  **Docker Login:** Authenticates to Docker Hub using repository secrets (`DOCKER_LOGIN`, `DOCKER_PWD`).
3.  **Build & Push:** Builds the Docker image and pushes it to Docker Hub with the `latest` tag.

## 🐳 Docker Hub

The application image is automatically built and hosted on Docker Hub.

- **Image URL:** [dockerjeremieo1/hello_world](https://hub.docker.com/r/dockerjeremieo1/hello_world)
- **Pull Command:**

```bash
docker pull dockerjeremieo1/hello_world:latest
```

## 📂 Project Structure

```text
MLops_Lab_5/
├── .github/workflows/   # CI/CD definitions (deploy, linter, test)
├── .gitignore           # Git ignore file
├── Dockerfile           # Docker image configuration
├── hello_world.py       # Main Flask Application
├── test_hello_world.py  # Unit Tests
├── requirements.txt     # Python dependencies
└── README.md            # Project Documentation
```
