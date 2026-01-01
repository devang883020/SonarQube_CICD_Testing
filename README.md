# 🚀 Production-Grade CI/CD GitOps Pipeline with Jenkins, SonarQube & Kubernetes

This project demonstrates a real-world DevOps CI/CD pipeline using GitOps principles to automate testing, code quality checks, containerization, and Kubernetes deployments on AWS.

The goal of this project is to showcase how modern DevOps teams safely ship code to production using automation, quality gates, and declarative infrastructure.

# 🧠 What Problem Does This Project Solve?

In real production systems:

Code should not be deployed blindly

Every change must pass tests & quality checks

Deployments must be reproducible and auditable

CI and CD responsibilities should be clearly separated

This project solves these problems by implementing:

Automated CI with Jenkins

Code Quality Gates using SonarQube

Immutable Docker images

GitOps-based CD using Helm + ArgoCD

# 🏗️ Architecture Overview

Developer → GitHub → Jenkins (CI)

                    ├─ Tests + Coverage
                    ├─ SonarQube Quality Gate
                    ├─ Docker Build & Push
                    └─ Update Helm values (GitOps)
                                   ↓
                              ArgoCD (CD)
                                   ↓
                           Kubernetes (EKS)
                                   ↓
                         LoadBalancer Service

# 🔄 Complete Project Flow

Code Push

Developer pushes code to GitHub

GitHub webhook triggers Jenkins

Continuous Integration (Jenkins)

Creates Python virtual environment

Runs unit tests with pytest

Generates code coverage report

Performs SonarQube static code analysis

Enforces Quality Gate

Pipeline stops if quality gate fails

Containerization

Jenkins builds Docker image

Image is pushed to Docker Hub

GitOps Update

Jenkins updates Docker image tag in Helm values.yaml

Change is committed to Git repository

Continuous Deployment (ArgoCD)

ArgoCD detects Git changes

Syncs Helm chart automatically

Deploys application to Kubernetes

Application Access

App is exposed using Kubernetes LoadBalancer Service

# 🛠️ Tools & Technologies Used
Category	Tools
CI	Jenkins
Code Quality	SonarQube
Testing	Pytest + Coverage
Containerization	Docker
Image Registry	Docker Hub
Packaging	Helm
CD	ArgoCD
Orchestration	Kubernetes (EKS)
Cloud	AWS
SCM	GitHub

# 🔐 Security & Best Practices

Credentials managed using Jenkins Credentials Store

SonarQube authentication via token

Docker Hub login via secure credentials

GitOps ensures no direct cluster access from Jenkins

Quality gates prevent bad code reaching production



# ✅ Key Highlights

Production-style CI/CD pipeline

GitOps-based Kubernetes deployments

Automated quality enforcement

No manual deployments

Real-world DevOps workflow

# 🎯 Why This Project Matters

This project reflects how CI/CD works in actual production environments, not just tutorials:

Clear separation of CI & CD

Safe deployments

Scalable Kubernetes architecture

Industry-standard tooling
