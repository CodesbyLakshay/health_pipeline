# Health Metrics Data Pipeline

A scalable data pipeline designed to process real-time health metrics for analysis. This project generates synthetic health data, performs ETL (Extract, Transform, Load) operations using Python and Luigi, and stores the processed data in an SQLite database for querying meaningful insights.

## Objective
The goal is to create an efficient pipeline that:
- Generates or processes health metrics for at least 500 individuals.
- Cleans and preprocesses the data.
- Stores it in an optimized SQLite database.
- Extracts actionable health insights via SQL queries.
- Automates the ETL process with Luigi.

## Project Structure
- **`generate_data.py`**: Generates synthetic health data for 500 individuals.
- **`etl_pipeline.py`**: Defines Luigi tasks for ETL (data generation, cleaning, loading into SQLite).
- **`run_queries.py`**: Executes SQL queries to extract insights from the database.

## Data
- **`health_data_clean.csv`**: Generates synthetic health data for 500 individuals.
- **`health_data_raw.csv`**: Defines Luigi tasks for ETL (data generation, cleaning, loading into SQLite).
- **`health_metrics.db`**: Executes SQL queries to extract insights from the database.

## Requirements
- Python 3.6+
- Libraries: `pandas`, `numpy`, `luigi`, `sqlite3` (built-in)
- Install dependencies:
  ```sh
  pip3 install pandas numpy luigi
