import json
import random
import time
from datetime import datetime
from kafka import KafkaProducer

TOPIC = "sensor_readings"
BOOTSTRAP_SERVERS = "localhost:29092" 

def create_producer():
    return KafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        linger_ms=50,
        retries=5,
    )

def generate_sensor_event(sensor_id: str):
    return {
        "sensor_id": sensor_id,
        "temperature": round(random.uniform(15.0, 35.0), 2),
        "humidity": round(random.uniform(30.0, 90.0), 2),
        "ts": datetime.utcnow().isoformat(timespec="seconds"),
    }

if __name__ == "__main__":
    producer = create_producer()
    sensors = [f"sensor-{i}" for i in range(1, 6)]
    print(f"Producing to topic '{TOPIC}' on {BOOTSTRAP_SERVERS} ... Ctrl+C to stop.")

    try:
        while True:
            event = generate_sensor_event(random.choice(sensors))
            producer.send(TOPIC, event)
            print("->", event)
            time.sleep(0.5)  
    except KeyboardInterrupt:
        print("\nStopping producer...")
    finally:
        producer.flush()
        producer.close()
