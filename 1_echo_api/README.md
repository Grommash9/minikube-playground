What should be done to build and deploy api


Build and push image to remote repo:

docker build -t api-app:latest .
docker tag api-app:latest docker.io/prudnikov21/api-app:latest
docker push docker.io/prudnikov21/api-app:latest

# It's probably not related to app but for local setup itself
kubectl config use-context minikube

kubectl apply -f echo-api-deployment.yaml
>> deployment.apps/api-app created

kubectl expose deployment api-app --type=NodePort --port=8000
>> service/api-app exposed

kubectl get services
>> NAME             TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
>> api-app          NodePort    10.102.174.215   <none>        8000:31602/TCP   30s

kubectl port-forward service/api-app 7000:8000
>> Forwarding from 127.0.0.1:7000 -> 8000
>> Forwarding from [::1]:7000 -> 8000
>> Handling connection for 7000
>> Handling connection for 7000