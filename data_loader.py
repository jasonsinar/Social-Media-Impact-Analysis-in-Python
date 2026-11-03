import csv
import os
from models import CSV_FILENAME, MAX_ROWS, Record


def load_data():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), CSV_FILENAME)

    if not os.path.isfile(path):
        print("File CSV tidak ditemukan.")
        return []

    records = []
    skipped = 0

    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for i, raw in enumerate(reader):
            if i >= MAX_ROWS:
                break
            try:
                rec = parse_row(raw)
                records.append(rec)
            except (ValueError, KeyError):
                skipped += 1

    print(f"Berhasil memuat {len(records)} data.")
    if skipped > 0:
        print(f"Melewati {skipped} baris yang tidak valid.")

    return records


def parse_row(raw):
    return Record(
        age=int(raw["Age"].strip()),
        platform=raw["Primary_Platform"].strip(),
        daily_hours=float(raw["Daily_Usage_Hours"].strip()),
        sleep_hours=float(raw["Sleep_Duration_Hours"].strip()),
        sleep_quality=int(raw["Sleep_Quality_Score"].strip()),
        late_night=raw["Late_Night_Usage"].strip().lower() == "true",
        impact=raw["Overall_Impact"].strip(),
    )
