import luigi
import pandas as pd
import sqlite3
import os

class GenerateDataTask(luigi.Task):
    data_path = luigi.Parameter(default="data/health_data_raw.csv")

    def output(self):
        return luigi.LocalTarget(self.data_path)

    def run(self):
        os.makedirs(os.path.dirname(self.data_path), exist_ok=True)
        import generate_data
        generate_data.generate_health_data(self.data_path)

class CleanDataTask(luigi.Task):
    raw_path = luigi.Parameter(default="data/health_data_raw.csv")
    clean_path = luigi.Parameter(default="data/health_data_clean.csv")

    def requires(self):
        return GenerateDataTask(data_path=self.raw_path)

    def output(self):
        return luigi.LocalTarget(self.clean_path)

    def run(self):
        df = pd.read_csv(self.raw_path)
        # Handle missing values
        df.fillna({
            "heart_rate": df["heart_rate"].mean(),
            "glucose_level": df["glucose_level"].mean(),
            "steps_count": 0,
            "calories_burn": df["calories_burn"].mean(),
            "sleep_duration": df["sleep_duration"].mean(),
        }, inplace=True)
        # Remove outliers (e.g., heart rate > 120 or < 50)
        df = df[(df["heart_rate"].between(50, 120)) & (df["glucose_level"].between(70, 140))]
        df.to_csv(self.clean_path, index=False)

class HealthMetricsLoadTask(luigi.Task):
    clean_path = luigi.Parameter(default="data/health_data_clean.csv")
    db_path = luigi.Parameter(default="data/health_metrics.db")

    def requires(self):
        return CleanDataTask(clean_path=self.clean_path)

    def output(self):
        return luigi.LocalTarget(self.db_path)

    def run(self):
        df = pd.read_csv(self.clean_path)
        conn = sqlite3.connect(self.db_path)
        # Optimized schema
        df.to_sql("health_metrics", conn, if_exists="replace", index=False, dtype={
            "individual_id": "INTEGER",
            "timestamp": "TEXT",
            "heart_rate": "REAL",
            "glucose_level": "REAL",
            "activity_level": "TEXT",
            "steps_count": "INTEGER",
            "calories_burn": "REAL",
            "sleep_duration": "REAL",
            "sleep_quality": "TEXT",
            "meal_intake": "TEXT"
        })
        # Create indexes for faster queries
        conn.execute("CREATE INDEX idx_individual ON health_metrics (individual_id)")
        conn.execute("CREATE INDEX idx_timestamp ON health_metrics (timestamp)")
        conn.close()