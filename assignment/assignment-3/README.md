# Introduction

The task in this assignment is to simulate data partitioning approaches using PostgreSQL. Each student must generate a set of Python functions that load the input data into a relational table, and partition the table using two different horizontal fragmentation approaches. The fragmentation approaches that will be taken in this assignment are range and round-robin partitioning, some more details to the same can be found [here](https://www.ibm.com/support/knowledgecenter/en/SSZJPZ_11.7.0/com.ibm.swg.im.iis.ds.parjob.dev.doc/topics/partitioning.html):

# Problem Statement

We will be using the subreddits.csv file and the created_utc column to create partitioned tables, this will be maintained for the grading as well. To make it easier to follow, we have divided this problem statement into a series of steps needed in order to get everything up and running. High-level information about each function below has also been made available in the assignment3.py file as docstrings:

1. Step 1: Loading the data
2. Step 2: Range Partition
3. Step 3: Round Robin Partition
