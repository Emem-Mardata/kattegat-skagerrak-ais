import csv
from datetime import datetime

days = ["2026-10-05", "2026-10-06", "2026-10-07", "2026-10-08", "2026-10-09", "2026-10-10", "2026-10-11"]

for day in days:
    with open("C:/GIS/Data/AIS/raw/aisdk-" + day + "/aisdk-" + day + ".csv", "r") as myfile, open("C:/GIS/Data/AIS/processed/aisdk-" + day + "_box.csv", "w", newline="") as outfile:
        reader = csv.reader(myfile)
        writer = csv.writer(outfile)
        headings = next(reader)
        writer.writerow([headings[0], headings[1], headings[2], headings[3], headings[4], headings[5], headings[7], headings[13], headings[16]])
        total = 0
        kept = 0
        for row in reader:
            total += 1
            lat = float(row[3])
            lon = float(row[4])
            if 54.63 <= lat <= 59.92 and 6.99 <= lon <= 13.07:
                kept += 1
                t = datetime.strptime(row[0], "%d/%m/%Y %H:%M:%S")
                iso = t.strftime("%Y-%m-%d %H:%M:%S")
                writer.writerow([iso, row[1], row[2], row[3], row[4], row[5], row[7], row[13], row[16]])
        print(day, total, kept)

   