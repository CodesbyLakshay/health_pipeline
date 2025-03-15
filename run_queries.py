import sqlite3
import argparse

def run_queries(db_path):
    conn = sqlite3.connect(db_path)
    queries = [
        ("Average heart rate per activity level", 
         "SELECT activity_level, AVG(heart_rate) FROM health_metrics GROUP BY activity_level"),
        ("Top 5 individuals by steps count", 
         "SELECT individual_id, SUM(steps_count) as total_steps FROM health_metrics GROUP BY individual_id ORDER BY total_steps DESC LIMIT 5"),
        ("Sleep duration vs. glucose level correlation", 
         "SELECT AVG(sleep_duration), AVG(glucose_level) FROM health_metrics GROUP BY individual_id"),
        ("Daily calories burned trend", 
         "SELECT DATE(timestamp), AVG(calories_burn) FROM health_metrics GROUP BY DATE(timestamp)"),
        ("Sleep quality distribution", 
         "SELECT sleep_quality, COUNT(*) FROM health_metrics GROUP BY sleep_quality"),
        ("Meal intake vs. activity level", 
         "SELECT meal_intake, activity_level, COUNT(*) FROM health_metrics GROUP BY meal_intake, activity_level"),
        ("High glucose outliers", 
         "SELECT individual_id, timestamp, glucose_level FROM health_metrics WHERE glucose_level > 130 ORDER BY glucose_level DESC LIMIT 10"),
    ]
    for title, query in queries:
        print(f"\n{title}:")
        result = conn.execute(query).fetchall()
        for row in result:
            print(row)
    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", required=True)
    args = parser.parse_args()
    run_queries(args.db)