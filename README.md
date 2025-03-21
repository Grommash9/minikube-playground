# minikube-playground

Building sample App


eval $(minikube -p addontest docker-env)

docker build -t hello-minikube:latest .


kubectl apply -f hello-minikube-deployment.yaml

kubectl get pods

kubectl get deployments


kubectl expose deployment hello-minikube --type=NodePort --port=8080

kubectl port-forward service/hello-minikube 7080:8080

http://localhost:7080

~~~~~~~~~~~~~~~~~~

kubectl proxy
#############
http://localhost:8001/api/v1/namespaces/default/services/hello-minikube:8080/proxy/


~~~~~~~~~~~~~~

Service Access
##############
minikube ssh

ssh -i ~/.minikube/machines/minikube/id_rsa docker@$(minikube ip)

~~~~~~~~~~~

Kubernetes Version
##################



minikube start --memory 2048 --cpus 2 --driver=docker -p k8sversion --kubernetes-version=v1.23.0
minikube stop -p k8sversion


minikube start --memory 2048 --cpus 2 --driver=docker -p k8sversion --kubernetes-version=v1.24.0

minikube delete -p k8sversion


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ingress - Demo
##############
minikube addons enable ingress



kubectl apply -f web-app-deployment.yaml
kubectl apply -f web-app-service.yaml
kubectl apply -f web-app-ingress.yaml


minikube ip


hosts file (/etc/hosts on Linux and macOS, C:\Windows\System32\drivers\etc\hosts on Windows)

<Minikube-IP> web-app.local


kubectl get pods -n ingress-nginx | grep ingress

kubectl get deployments

kubectl get svc

kubectl get ingress

kubectl describe ingress web-app-ingress


kubectl delete -f web-app-deployment.yaml
kubectl delete -f web-app-service.yaml
kubectl delete -f web-app-ingress.yaml



~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

netstat -ato

~~~~~~~~~~~~~~~~~~~

host vs path based routing


<minikube-ip> api.minikube.local
<minikube-ip> web.minikube.local

#Local ip if minikube running as docker container in docker desktop

curl http://api.minikube.local
curl http://web.minikube.local/web
curl http://web.minikube.local/api