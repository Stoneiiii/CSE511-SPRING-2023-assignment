# Introduction

RocksDB is an embeddable persistent key-value store for fast storage environments. It uses a log structured database engine, written entirely in C++ for maximum performance. Over the years, RocksDB has become a popular choice for a wide range of applications, including large-scale data processing, real-time analytics, and high-throughput transaction processing. It is used by companies such as Facebook, and LinkedIn to power their critical data-driven applications. From database storage engines such as MyRocks to application data caching to embedded workloads, RocksDB can be used for a variety of data needs. It provides basic operations such as opening and closing a database, reading and writing to more advanced operations such as merging and compaction filters. For this assignment, we will be exploring the more basic functionalities of this Key-Value Store.

# Problem Statement

In the scope of this assignment, we will use subreddits.csv of the Reddit database from the previous assignments. The subreddits.csv is also available [here](https://www.dropbox.com/sh/3ixxc9c7jm1rjrq/AACKrpX76iKMtyFX_oYbca7Aa?dl=0&preview=subreddits.csv). Also in this assignment, only high-level steps and expectations are mentioned. You are expected to explore the necessary requirements to solve the problem statement.

1. Step 0: Creating the setup for RocksDB
2. Step 1: Loading the Data
3. Step 2: Basic Operations
   1. Read
   2. Iterator
   3. Delete
      
