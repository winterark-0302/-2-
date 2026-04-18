#!/bin/bash

echo -e "\033[1;36m=============================================\033[0m"
echo -e "\033[1;36m       SafeK Deployment Automation Tool      \033[0m"
echo -e "\033[1;36m=============================================\033[0m"
echo ""
echo "Please select a deployment target:"
echo "  1) Docker Compose (Local Environment)"
echo "  2) Kubernetes / Minikube (Cluster Environment)"
echo "  3) Clean Up All Environments"
echo "  4) Exit"
echo ""

read -p "Enter your choice (1-4): " choice

case $choice in
    1)
        echo -e "\033[1;32mDeploying SafeK via Docker Compose...\033[0m"
        docker-compose down
        docker-compose up -d --build
        if [ $? -eq 0 ]; then
            echo -e "\033[1;32mSuccess! The application is running.\033[0m"
            echo -e "\033[1;33mFrontend App:    http://localhost:8080\033[0m"
            echo -e "\033[1;33mGrafana Metrics:  http://localhost:3000\033[0m"
        else
            echo -e "\033[1;31mError: docker-compose deployment failed.\033[0m"
        fi
        ;;
    2)
        echo -e "\033[1;32mDeploying SafeK via Kubernetes...\033[0m"
        
        echo -e "\033[1;33mCreating dashboard ConfigMap from local JSON...\033[0m"
        kubectl create configmap grafana-dashboard-nginx --from-file=grafana/dashboards/nginx.json -n monitoring --dry-run=client -o yaml | kubectl apply -f -
        
        kubectl apply -f k8s/configmaps.yaml
        kubectl apply -f k8s/frontend-deployment.yaml
        kubectl apply -f k8s/frontend-service.yaml
        kubectl apply -f k8s/monitoring.yaml
        
        if [ $? -eq 0 ]; then
            echo -e "\033[1;32mSuccess! Kubernetes manifests applied.\033[0m"
            echo -e "\033[1;33mIf running locally (e.g., Minikube), you may need to port-forward or run 'minikube service list' to access:\033[0m"
            echo -e "\033[1;33mFrontend App:    NodePort 30080\033[0m"
            echo -e "\033[1;33mGrafana Metrics:  NodePort 30300\033[0m"
        else
            echo -e "\033[1;31mError: Kubernetes deployment failed.\033[0m"
        fi
        ;;
    3)
        echo -e "\033[1;33mCleaning up resources...\033[0m"
        echo "Tearing down Docker Compose..."
        docker-compose down
        echo "Tearing down Kubernetes resources..."
        kubectl delete -f k8s/monitoring.yaml --ignore-not-found=true
        kubectl delete -f k8s/frontend-service.yaml --ignore-not-found=true
        kubectl delete -f k8s/frontend-deployment.yaml --ignore-not-found=true
        kubectl delete -f k8s/configmaps.yaml --ignore-not-found=true
        echo -e "\033[1;32mClean up finished.\033[0m"
        ;;
    4)
        echo "Exiting."
        exit 0
        ;;
    *)
        echo -e "\033[1;31mInvalid choice. Exiting.\033[0m"
        exit 1
        ;;
esac
