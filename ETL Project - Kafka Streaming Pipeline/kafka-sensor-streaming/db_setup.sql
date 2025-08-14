CREATE TABLE IF NOT EXISTS sensor_data (
    id SERIAL PRIMARY KEY,
    sensor_id VARCHAR(50) NOT NULL,
    temperature DOUBLE PRECISION,
    humidity DOUBLE PRECISION,
    ts TIMESTAMP NOT NULL
);