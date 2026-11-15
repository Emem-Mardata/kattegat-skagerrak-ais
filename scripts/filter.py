import csv
import os
from datetime import datetime

# Set BASE to the folder holding your AIS data, or set the AIS_BASE
# environment variable. The layout below is expected underneath it:
#   <BASE>/raw/aisdk-<day>/aisdk-<day>.csv      input, unzipped
#   <BASE>/processed/aisdk-<day>_box.csv        output
BASE = os.environ.get("AIS_BASE", r"C:/GIS/Data/AIS")

days = ["2026-10-05", "2026-10-06", "2026-10-07", "2026-10-08", "2026-10-09", "2026-10-10", "2026-10-11"]

for day in days:
    infile = os.path.join(BASE, "raw", "aisdk-" + day, "aisdk-" + day + ".csv")
    outfile = os.path.join(BASE, "processed", "aisdk-" + day + "_box.csv")
    with open(infile, "r") as myfile, open(outfile, "w", newline="") as out:
        reader = csv.reader(myfile)
        writer = csv.writer(out)
        headings = next(reader)
        writer.writerow([headings[0], headings[1], headings[2], headings[3], headings[4], headings[5], headings[7], headings[13], headings[16]])
        total = 0
        kept = 0
        skipped = 0
        for row in reader:
            total += 1
            try:
                lat = float(row[3])
                lon = float(row[4])
            except (ValueError, IndexError):
                skipped += 1          # unreadable position: counted, not silently dropped
                continue
            if 54.63 <= lat <= 59.92 and 6.99 <= lon <= 13.07:
                kept += 1
                t = datetime.strptime(row[0], "%d/%m/%Y %H:%M:%S")
                iso = t.strftime("%Y-%m-%d %H:%M:%S")
                writer.writerow([iso, row[1], row[2], row[3], row[4], row[5], row[7], row[13], row[16]])
        print(day, total, kept, skipped)
