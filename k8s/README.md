```bash
kubectl apply -f=k8s_deployment.yaml -f=k8s_service.yaml
kubectl get pods
kubectl get deployment
minikube service weatherapp-service
minikube dashboard

kubectl describe pod weatherapp-deployment-6bf8f947d5-j4f9h     # pod name
kubectl exec -it weatherapp-deployment-6bf8f947d5-j4f9h -c weatherclient-app-container -- /bin/bash

# inside container
cat /data/weather.txt

Sun Aug 31 16:23:54 2025: {'city': 'Belgrade', 'temperature': '19.38°C'}
Sun Aug 31 16:25:54 2025: {'city': 'Belgrade', 'temperature': '18.97°C'}
Sun Aug 31 16:27:54 2025: {'city': 'Belgrade', 'temperature': '19.38°C'}
exit

# on host
kubectl delete -f=k8s_deployment.yaml -f=k8s_service.yaml

```