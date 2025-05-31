CREATE TABLE covid_stats (
    country VARCHAR(255),
    cases INT,
    deaths INT,
    recovered INT,
    updated TIMESTAMP,
    ingestion_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);