import pandas as pd
import numpy as np
import argparse
from datetime import datetime, timedelta

def generate_health_data(output_path):
    np.random.seed(42)
    n_individuals = 500
    n_records = n_individuals * 10  # 10 records per individual

    data = {
        "individual_id": np.repeat(range(1, n_individuals + 1), 10),
        "timestamp": [datetime.now() - timedelta(minutes=i * 60) for i in range(n_records)],
        "heart_rate": np.random.normal(75, 10, n_records).clip(50, 120),
        "glucose_level": np.random.normal(90, 15, n_records).clip(70, 140),
        "activity_level": np.random.choice(["low", "medium", "high"], n_records),
        "steps_count": np.random.randint(0, 15000, n_records),
        "calories_burn": np.random.normal(2000, 500, n_records).clip(1500, 3600),
        "sleep_duration": np.random.normal(7, 1, n_records).clip(4, 10),
        "sleep_quality": np.random.choice(["poor", "fair", "good"], n_records),
        "meal_intake": np.random.choice(["light", "moderate", "heavy"], n_records),
    }
    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    print(f"Generated data saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    generate_health_data(args.output)