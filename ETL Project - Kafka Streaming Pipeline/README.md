# **ETL Streaming Project – Kafka Sensor Data**

## **Objective**
This project demonstrates real-time data ingestion and storage using **Apache Kafka** and **PostgreSQL**.  
It simulates IoT sensor data being produced continuously, consumed in real time, and stored in a relational database.

---

## **Features**
- **Kafka Producer** simulating continuous sensor readings.  
- **Kafka Consumer** receiving and inserting data into PostgreSQL.  
- Complete **ingestion → processing → storage** streaming pipeline.  
- Ready-to-run local environment with Docker.

---

## **Technologies Used**
- **Apache Kafka** – Real-time streaming platform.  
- **Python** – For producer and consumer scripts.  
- **PostgreSQL** – Relational database for storing processed data.  
- **Docker** – Local environment setup.  

---

## **Project Structure**
- producer.py # Simulates sensors, sends data to Kafka.
- consumer.py # Consumes data from Kafka and stores in PostgreSQL.
- db_setup.sql # Creates the PostgreSQL table.
- docker-compose.yml # Starts Kafka, Zookeeper, PostgreSQL.

---

## **How to Run**

1. Start Kafka and PostgreSQL
docker compose up -d

2. Create the database table
docker exec -it postgres-sensors psql -U admin -d sensors -f db_setup.sql

3. Start the Kafka Producer
python producer.py
This script continuously sends simulated sensor data to the Kafka topic.

4. Start the Kafka Consumer
Open a new terminal and run:
python consumer.py
The consumer listens for incoming messages and inserts them into PostgreSQL.

5. Verify Data in PostgreSQL
To check if data is being stored:
docker exec -it postgres-sensors psql -U admin -d sensors -c "SELECT COUNT(*) FROM sensor_data;"
