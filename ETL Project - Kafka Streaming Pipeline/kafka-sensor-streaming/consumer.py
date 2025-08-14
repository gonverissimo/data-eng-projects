import json
import psycopg2
from kafka import KafkaConsumer

TOPIC = "sensor_readings"
BOOTSTRAP_SERVERS = "localhost:29092"

DB_CONN = {
    "host": "localhost",
    "port": 5432,
    "dbname": "sensors",
    "user": "admin",
    "password": "admin",
}

def get_db_conn():
    return psycopg2.connect(**DB_CONN)

def main():
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="sensor-consumers",
    )
    print(f"Consuming from '{TOPIC}' ... Ctrl+C to stop.")

    conn = get_db_conn()
    conn.autocommit = True
    cur = conn.cursor()

    try:
        for msg in consumer:
            data = msg.value
            cur.execute(
                """
                INSERT INTO sensor_data (sensor_id, temperature, humidity, ts)
                VALUES (%s, %s, %s, %s)
                """,
                (data["sensor_id"], data["temperature"], data["humidity"], data["ts"]),
            )
            print("<-", data)
    except KeyboardInterrupt:
        print("\nStopping consumer...")
    finally:
        cur.close()
        conn.close()
        consumer.close()

if __name__ == "__main__":
    main()
