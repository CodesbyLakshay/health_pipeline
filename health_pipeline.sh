#!/bin/bash

# Health Metrics Data Pipeline Script
# Requirements: Python 3, pip3, SQLite (built-in), Luigi
# Usage: chmod +x health_pipeline.sh && ./health_pipeline.sh

# Set project directory
PROJECT_DIR="$(pwd)"
DATA_DIR="$PROJECT_DIR/data"

# Update these paths based on your system
PYTHON_BIN="/Library/Frameworks/Python.framework/Versions/3.13/bin/python3"  # Adjust if needed
PIP_BIN="/Library/Frameworks/Python.framework/Versions/3.13/bin/pip3"       # Adjust if needed

# Create data directory if it doesn’t exist
mkdir -p "$DATA_DIR"

# Step 1: Install dependencies
echo "Installing Python dependencies..."
$PIP_BIN install --user pandas numpy luigi
sleep 5  # Ensure install completes

# Step 2: Generate synthetic health data
echo "Generating synthetic health data..."
$PYTHON_BIN generate_data.py --output "$DATA_DIR/health_data_raw.csv"

# Step 3: Run Luigi ETL pipeline (clean, transform, load)
echo "Running Luigi ETL pipeline..."
$PYTHON_BIN -m luigi --module etl_pipeline HealthMetricsLoadTask --local-scheduler

# Step 4: Run SQL queries for insights
echo "Running SQL queries for insights..."
$PYTHON_BIN run_queries.py --db "$DATA_DIR/health_metrics.db"

echo "Pipeline completed! Check $DATA_DIR for outputs."