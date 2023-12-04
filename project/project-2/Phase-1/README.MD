# Introduction & Background

Graph-based data is ubiquitous and has various applications, such as examining the structure of the internet, bioinformatics data representation, chemistry, and distributed computation. Academia and industry collaborations have developed their own graph processing systems to handle massive graphs. Graph-processing tasks involve using specific algorithms to extract various properties from graphs, such as computing important vertices with PageRank or identifying large communities using different algorithms. These algorithms are typically executed in parallel when resources are available. When implementing such algorithms, developers must consider challenges such as parallelism and the use of underlying frameworks. In this project, we will explore how to implement graph processing algorithms in both non-distributed and distributed deployment environments.

# Problem Statement

In Phase 1 of this project, you will be learning to create Docker containers that install neo4j and will be implementing two Graph algorithms in neo4j. For this project, we will use the NYC Yellow Cab Trip dataset. To make it easy to follow, we have divided this assignment into 4 broad steps that will help you understand the topics and complete the project.

- Step 0: Exploring the world of Graph Databases

	Graph databases use specialized data structures and algorithms to efficiently traverse and query these graph structures. Graph databases are well-suited for highly interconnected data, such as social networks, recommendation engines, fraud detection, and knowledge management

- Step 1: Setting up the Dockerfile and Loading the data

	This step of the project will explore loading data into neo4j and what a Dockerfile looks like. By the end of this step, you should be able to explore your neo4j environment with the loaded data and have a basic grasp on creating the Docker containers we have been using the last few assignments.

- Step 2: Setting up required neo4j plugin

	You are permitted to install and use any neo4j plugin you want to use for this phase of the project. In this step, you will perform installation of the neo4j GDS plugin from the Dockerfile . The GDS (graph data science) plugin adds several basic and useful procedure calls to neo4j, and more specifically, it adds procedure calls for Step 3.

- Step 3: Implementing Graph Algorithms

	Now, when you have your Neo4j development setup is ready on a container instance, the next step is to implement the twp Graph Algorithms mentioned below. These algorithms need to be implemented in the interface.py file in their respective functions. The interface.py file does not need to be inside the container and will connect to the docker container from outside it. I.e. using the 7687 port that we have exposed from inside docker.

	1. PageRank
	2. Breadth First Search

