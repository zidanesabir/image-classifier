# Image Classification with MobileNet on Minikube

This project implements an image classification system using MobileNetV2, containerized with Docker, and deployed on Minikube. It includes a FastAPI backend for serving predictions and a simple web UI for uploading images.

## Project Structure

```
image-classifier/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   └── endpoints.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── model.py
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   ├── templates/
│   │   └── index.html
│   ├── __init__.py
│   └── main.py
├── kubernetes/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── hpa.yaml
├── load-testing/
│   └── locustfile.py
├── .gitignore
├── Dockerfile
├── requirements.txt
├── PERFORMANCE.md
└── README.md
```

## Features

- **Image Classification API**: FastAPI-based REST API for image classification
- **Pre-trained MobileNetV2 Model**: Efficient CNN optimized for deployment
- **Web UI**: Simple and responsive interface for uploading images and viewing predictions
- **Kubernetes Deployment**: Configured for Minikube with autoscaling capabilities
- **Docker Containerization**: Packaged for consistent deployment

## Requirements

- Python 3.9+
- Docker
- Minikube
- kubectl

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/image-classifier.git
cd image-classifier
```

### 2. Local Development Setup

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Run the application locally:

```bash
python -m app.main
```

The application will be available at http://localhost:8000

### 3. Building the Docker Image

```bash
docker build -t image-classifier:latest .
```

Test the Docker container locally:

```bash
docker run -p 8000:8000 image-classifier:latest
```

### 4. Deploying on Minikube

Start Minikube:

```bash
minikube start
```

Point your Docker CLI to the Minikube Docker daemon:

```bash
eval $(minikube -p minikube docker-env)  # On Windows: & minikube -p minikube docker-env | Invoke-Expression
```

Build the Docker image in the Minikube environment:

```bash
docker build -t image-classifier:latest .
```

Apply Kubernetes manifests:

```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
kubectl apply -f kubernetes/hpa.yaml
```

Access the application:

```bash
minikube service image-classifier
```



## Performance Testing

To run performance tests using Locust:

```bash
cd load-testing
mkdir -p sample_images
# Add some sample images to the sample_images directory
pip install locust
locust -f locustfile.py
```

Open http://localhost:8089 to access the Locust UI.

## Performance Optimization

See [PERFORMANCE.md](PERFORMANCE.md) for detailed performance metrics and optimization strategies.

## Implementation Details

### Model Service

The system uses MobileNetV2 pre-trained on ImageNet for efficient image classification:

- Optimized for edge and mobile devices
- 1000 object classes from ImageNet dataset
- Small model size (~14MB)
- Fast inference time suitable for real-time applications

### API Layer

FastAPI provides a modern, high-performance API with:

- Automatic OpenAPI documentation
- Request validation
- Efficient async handling
- Health checks and monitoring

### Kubernetes Deployment

The application is deployed on Minikube with:

- Horizontal Pod Autoscaler for automatic scaling
- Rolling updates for zero-downtime deployments
- Resource limits and requests for optimal performance
- Readiness and liveness probes for reliability

## Future Improvements

- Implement model quantization for better CPU performance
- Add batch processing capabilities
- Explore model pruning for smaller deployment size
- Implement caching for frequent requests
- Add authentication and rate limiting

## License

This project is licensed under the MIT License - see the LICENSE file for details.
## projet UI 
![Capture d’écran 2025-05-08 235222](https://github.com/user-attachments/assets/3043428a-f809-4b4b-bf85-cf324b569a2d)
![image](https://github.com/user-attachments/assets/44e38f97-0ddd-4e88-9188-cc6cc217ebe8)
![image](https://github.com/user-attachments/assets/c7d8449a-bf48-43d8-9ac7-d21c25c2a726)
![image](https://github.com/user-attachments/assets/28f2a029-736b-4d50-881a-e0eb55821fbf)



## Author

zidane sabir  - [sabirzidane0@gmail.com]
