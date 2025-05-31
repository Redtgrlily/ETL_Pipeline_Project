COVID-19 ETL Pipeline Project
Overview
This project demonstrates a robust, production-like ETL pipeline designed to:

Extract COVID-19 data from a public API (disease.sh)

Transform the raw data using Pandas for cleaning and normalization

Load the transformed data into a PostgreSQL relational database

Orchestrate the entire pipeline with Apache Airflow, scheduled to run daily

Visualize the results via Tableau connected to the PostgreSQL database

Tech Stack
Layer	Technology
Extraction	Python, requests
Transformation	Python, Pandas
Loading	PostgreSQL, SQLAlchemy
Orchestration	Apache Airflow
Containerization	Docker
Visualization	Tableau

Motivation & Key Challenge
One of the top challenges data engineers face is building reliable, maintainable pipelines that automate the entire data flow — from raw external sources to actionable insights — while ensuring reproducibility and easy orchestration. This project demonstrates tackling this with:

Modular Python scripts

Containerized, reproducible environments

Automated scheduling and retries with Airflow

Scalable relational storage in PostgreSQL

Industry-grade BI visualization in Tableau

Project Structure
graphql
Copy
Edit
covid_etl_project/
├── dags/
│   └── covid_etl_dag.py        # Airflow DAG to orchestrate ETL
├── scripts/
│   ├── extract.py              # Extract raw data from API
│   ├── transform.py            # Transform data using Pandas
│   └── load.py                 # Load data into PostgreSQL
├── airflow/
│   └── Dockerfile              # Custom Airflow image with dependencies
├── db/
│   └── init.sql                # Database schema initialization script
├── docker-compose.yml          # Docker Compose to run Airflow + Postgres
├── requirements.txt            # Python dependencies
└── README.md                   # This file
Getting Started
Prerequisites
Docker Desktop (macOS, Windows, Linux)

Tableau Desktop (for visualization)

Git

Setup
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/covid_etl_project.git
cd covid_etl_project
Build and run Docker containers

bash
Copy
Edit
docker compose up --build
This will start PostgreSQL on port 5432 and Airflow on port 8080.

Airflow will initialize its metadata database and start scheduler + webserver.

Initialize database schema

Access PostgreSQL to create the required table:

bash
Copy
Edit
docker exec -it postgres psql -U airflow -d etl_db -f /path/to/db/init.sql
Or connect with any PostgreSQL client using:

Host: localhost

Port: 5432

User: airflow

Password: airflow

Database: etl_db

Access Airflow UI

Open your browser:

arduino
Copy
Edit
http://localhost:8080
Login with:

Username: airflow

Password: airflow

Trigger ETL DAG

Enable the covid_etl_dag from the Airflow UI.

Manually trigger the DAG or wait for the scheduled daily run.

Connect Tableau

Connect Tableau to PostgreSQL using the same connection details as above.

Visualize the covid_stats table and create your dashboards.

Key Files Explained
scripts/extract.py: Fetches raw COVID-19 data via API

scripts/transform.py: Cleans and structures data with Pandas

scripts/load.py: Pushes the transformed data to PostgreSQL

dags/covid_etl_dag.py: Defines the Airflow DAG orchestrating ETL

docker-compose.yml: Orchestrates multi-container Docker environment

airflow/Dockerfile: Custom Airflow image with necessary Python packages

db/init.sql: SQL schema for covid_stats table in PostgreSQL

Challenges & Solutions
Dependency management in Airflow containers: solved by custom Docker image.

Ensuring data freshness and reliability: daily scheduled runs with retry.

API data variability and timestamp conversion: handled in Pandas transform step.

Seamless local setup for development and demonstration: Docker Compose orchestration.

Future Improvements
Add tests and data validation in the pipeline.

Improve API error handling and logging.

Extend pipeline with incremental updates instead of full overwrite.

Automate Tableau dashboard deployment.

Contact
Created by Kaitlyn McCormick — passionate about data engineering and automation.

Feel free to reach out or check more projects on GitHub.