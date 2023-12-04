# Base image: ubuntu:22.04
FROM ubuntu:22.04

# ARGs
# https://docs.docker.com/engine/reference/builder/#understand-how-arg-and-from-interact
ARG TARGETPLATFORM=linux/amd64,linux/arm64
ARG DEBIAN_FRONTEND=noninteractive

# neo4j 5.5.0 installation and some cleanup
RUN apt-get update && \
    apt-get install -y wget gnupg software-properties-common && \
    wget -O - https://debian.neo4j.com/neotechnology.gpg.key | apt-key add - && \
    echo 'deb https://debian.neo4j.com stable latest' > /etc/apt/sources.list.d/neo4j.list && \
    add-apt-repository universe && \
    apt-get update && \
    apt-get install -y nano unzip neo4j=1:5.5.0 python3-pip && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# TODO: Complete the Dockerfile
RUN mkdir /cse511
WORKDIR /cse511
RUN wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2022-03.parquet && \
    apt-get update && \
    apt-get install curl -y && \
    apt-get update && \
    curl -O https://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@raw.githubusercontent.com/CSE511-SPRING-2023/leihu3-project-2/main/data_loader.py && \
    python3 -m pip install --upgrade pip && \
    pip install neo4j && \
    pip install pandas && \
    pip install pyarrow && \
    neo4j-admin dbms set-initial-password project2phase1 

RUN neo4j start && \
    sleep 5 && \
    NEO4J_USERNAME=neo4j NEO4J_PASSWORD=project2phase1 cypher-shell --fail-fast && \
    neo4j stop

RUN sed -i 's/#server.default_listen_address=0.0.0.0/server.default_listen_address=0.0.0.0/g' /etc/neo4j/neo4j.conf && \
    sed -i 's/#server.bolt.listen_address=:7687/server.bolt.listen_address=:7687/g' /etc/neo4j/neo4j.conf && \
    sed -i 's/#server.bolt.advertised_address=:7687/server.bolt.advertised_address=:7687/g' /etc/neo4j/neo4j.conf && \
    sed -i 's/#server.http.listen_address=:7474/server.http.listen_address=:7474/g' /etc/neo4j/neo4j.conf && \
    sed -i 's/#server.http.advertised_address=:7474/server.http.advertised_address=:7474/g' /etc/neo4j/neo4j.conf && \
    sed -i '$adbms.security.procedures.unrestricted=gds.*' /etc/neo4j/neo4j.conf

RUN wget https://graphdatascience.ninja/neo4j-graph-data-science-2.3.2.zip && \
    apt-get install zip -y && \
    unzip neo4j-graph-data-science-2.3.2.zip -d /var/lib/neo4j/plugins/




# Run the data loader script
RUN chmod +x /cse511/data_loader.py && \
    neo4j start && \
    python3 data_loader.py && \
    neo4j stop

# Expose neo4j ports
EXPOSE 7474 7687

# Start neo4j service and show the logs on container run
CMD ["/bin/bash", "-c", "neo4j start && tail -f /dev/null"]
