param(
    [switch]$Help
)

if ($Help) {
    Write-Host "SafeK Deployment Automation Script"
    Write-Host "This script provides an interactive menu to deploy SafeK either via Docker Compose or Kubernetes."
    exit
}

Write-Host "=============================================" -ForegroundColor Cyan
Write-Host "       SafeK Deployment Automation Tool      " -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Please select a deployment target:"
Write-Host "  1) Docker Compose (Local Environment)"
Write-Host "  2) Kubernetes / Minikube (Cluster Environment)"
Write-Host "  3) Clean Up All Environments"
Write-Host "  4) Exit"
Write-Host ""

$choice = Read-Host "Enter your choice (1-4)"

switch ($choice) {
    "1" {
        Write-Host "Deploying SafeK via Docker Compose..." -ForegroundColor Green
        docker-compose down
        docker-compose up -d --build
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Success! The application is running." -ForegroundColor Green
            Write-Host "Frontend App:    http://localhost:8080" -ForegroundColor Yellow
            Write-Host "Grafana Metrics:  http://localhost:3000" -ForegroundColor Yellow
        } else {
            Write-Host "Error: docker-compose deployment failed." -ForegroundColor Red
        }
    }
    "2" {
        Write-Host "Deploying SafeK via Kubernetes..." -ForegroundColor Green
        
        Write-Host "Creating dashboard ConfigMap from local JSON..." -ForegroundColor Yellow
        # Create configmap from local file explicitly (dry run into apply)
        kubectl create configmap grafana-dashboard-nginx --from-file=grafana/dashboards/nginx.json -n monitoring --dry-run=client -o yaml | kubectl apply -f -
        
        # Apply ConfigMaps first
        kubectl apply -f k8s/configmaps.yaml
        # Apply Deployments and Services
        kubectl apply -f k8s/frontend-deployment.yaml
        kubectl apply -f k8s/frontend-service.yaml
        kubectl apply -f k8s/monitoring.yaml
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Success! Kubernetes manifests applied." -ForegroundColor Green
            Write-Host "If running locally (e.g., Minikube), you may need to port-forward or run 'minikube service list' to access:" -ForegroundColor Yellow
            Write-Host "Frontend App:    NodePort 30080" -ForegroundColor Yellow
            Write-Host "Grafana Metrics:  NodePort 30300" -ForegroundColor Yellow
        } else {
            Write-Host "Error: Kubernetes deployment failed. Please check your kubectl configuration." -ForegroundColor Red
        }
    }
    "3" {
        Write-Host "Cleaning up resources..." -ForegroundColor Yellow
        Write-Host "Tearing down Docker Compose..."
        docker-compose down
        
        Write-Host "Tearing down Kubernetes resources..."
        kubectl delete -f k8s/monitoring.yaml --ignore-not-found=true
        kubectl delete -f k8s/frontend-service.yaml --ignore-not-found=true
        kubectl delete -f k8s/frontend-deployment.yaml --ignore-not-found=true
        kubectl delete -f k8s/configmaps.yaml --ignore-not-found=true
        Write-Host "Clean up finished." -ForegroundColor Green
    }
    "4" {
        Write-Host "Exiting."
        exit
    }
    default {
        Write-Host "Invalid choice. Exiting." -ForegroundColor Red
    }
}
