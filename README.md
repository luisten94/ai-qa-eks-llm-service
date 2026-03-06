# AI Question Answering Service on AWS EKS

This project deploys a cloud-based AI question answering service using AWS and Kubernetes.

The system exposes a REST API built with FastAPI that sends user questions to a self-hosted LLM running with vLLM on an EKS cluster.

The infrastructure is fully provisioned using Terraform and the applications are deployed using Helm.

---

## Architecture

The architecture consists of the following components:

- FastAPI service
- vLLM model server
- AWS EKS Kubernetes cluster
- AWS ECR for container images
- Terraform for infrastructure provisioning
- Helm for Kubernetes deployments

Flow:

User → FastAPI API → vLLM → AI Response

FastAPI receives a question and forwards the request to the vLLM container which runs the SmolLM2-135M-Instruct model.

---

## Tech Stack

- Python
- FastAPI
- Docker
- AWS EKS
- Terraform
- Helm
- vLLM
- Kubernetes

---

## Infrastructure

Infrastructure is provisioned using Terraform and includes:

- VPC
- Public and private subnets
- Security groups
- IAM roles
- EKS cluster
- Node group

---

## Deployment Steps

### 1. Provision Infrastructure


terraform init
terraform apply


### 2. Configure kubectl


aws eks update-kubeconfig --region us-east-1 --name ai-qa-cluster


### 3. Deploy the services

FastAPI API:


helm install fastapi ./helm/fastapi


vLLM model:


helm install vllm ./helm/vllm


---

## API Endpoint

POST /ask

Example request:


{
"question": "What is Kubernetes?"
}


Example response:


{
"answer": "Kubernetes is a container orchestration platform..."
}


---

## Scaling Strategy

LLM workloads can be scaled using:

- Horizontal Pod Autoscaler
- Node group autoscaling
- GPU-based node groups
- Request batching
- Model sharding

In production environments GPU instances and autoscaling policies would be used to scale inference workloads.

---

## Notes

This project is a simplified architecture designed to demonstrate a production-style DevOps workflow using AWS and Kubernetes.