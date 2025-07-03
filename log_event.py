from datetime import datetime
import csv

def log_event(event_type, value, source):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [timestamp, event_type, value, source]

    with open("logs/events.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)

