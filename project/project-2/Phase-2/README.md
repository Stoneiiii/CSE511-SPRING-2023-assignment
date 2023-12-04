### Thanks for grading my project.
## Startup
```bash
#notice: minikube cann't be run in root
#set memory:8G cpu:3
minikube start --memory 8096 --cpus 3
```

## Step 1
Deployment of Zookeeper and Kafka
```bash
#deploy kafka and zookeeper
kubectl apply -f ./zookeeper-setup.yaml
kubectl apply -f ./kafka-setup.yaml
```

Kafka pod may run fail because it needs the Zookeeper environment. After the Zookeeper pod start completely, it will run successfully, due to Kubernetes will run Kafka pod continuously.

## Step 2
Deployment of Neo4j.
```bash
helm install my-neo4j-release neo4j/neo4j -f neo4j-values.yaml
kubectl apply -f neo4j-service.yaml
```

## Step 3
Deployment of the Kafka-Neo4j connection
```bash
kubectl apply -f kafka-neo4j-connector.yaml
```

## Step 4
Deployment of the entire pipeline with the interface file.
```bash
kubectl port-forward svc/neo4j-service 7474:7474 7687:7687
kubectl port-forward svc/kafka-service 9092:9092
python3 data_producer.py
python3 tester.py
```


