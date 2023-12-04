# Introduction

The last assignment explored Docker and neo4j. However, there are a drawbacks to that kind of a setup, specially in terms of scalability and availability. This phase of the project will specifically deal with this issue while also demonstrating how to create a data processing pipeline with multiple technologies in Kubernetes. Over the course of the assignment, you will be familiarized with technologies like Kubernetes and Kafka, all integrated with your previously gained knowledge of Docker and Neo4j.

# Problem Statement

You will be creating a highly scalable and highly available data processing pipeline that takes a document stream as its input and performs various processing operations on it before streaming it into a distributed neo4j setup to allow for near real-time processing and analytics.

This document has been designed to explore the pipeline one connection at a time. It is important to understand the motivation of every component as a unit and in tandem. The project document will guide you along the way while also encouraging self-exploration.

- Step 0: The Network Whisperer

	The most important part of this project is to understand how data is going to flow from Point A to Point B. This section will answer that question, and white everything may not be obvious on the very first glance, as every step passes, information given over here will start to gain value and help you along the way.
![image](https://github.com/Stoneiiii/CSE511-assignment/blob/main/project/project-2/Phase-2/images/image1.png)

- Step 1: Order in the Chaos

	In this step, you will set up the orchestrator and Kafka for your pipeline. The orchestrator is a tool that helps you manage the different components of your pipeline, such as data ingestion, processing, and storage. You will use minikube as your orchestrator, which is a lightweight Kubernetes implementation that runs locally on your machine. Kafka is a distributed streaming platform that helps you collect and process the incoming data streams. You will use Kafka to ingest data from the document stream and distribute it to other components of your pipeline. The following diagram shows what all should be set up by the end of this step.

- Step 2: Charting the way forward

	In this step, we will be implementing neo4j in our setup. You already have a firm grasp on neo4j and the ins and out of its container. However, for this project, since the data will be streamed, we can simply utilize neo4j setups that are available for Kubernetes.

- Step 3: Neo4j -> [<3] -> Kafka

	In this step, Kafka and Neo4j will be connected. There are tools already available for this, specifically the kafka connect extension that we will utilize.

- Step 4: PA T PB

	By this step, you should have everything put together. You can try to run the data_producer.py file provided to you at this point. The data should have a high-level flow in the following manner: producer => enter kubernetes environment => (kbe) kafka => (kbe) neo4j => exit kubernetes environment => data analytics. The same two algorithms from phase 1 of the project will be utilized again: PageRank, and Breadth-First Search (BFS). You need to implement them in the interface.py file provided.

# Usage
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


