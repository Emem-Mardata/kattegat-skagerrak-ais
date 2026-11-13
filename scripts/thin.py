import csv
days = ["2026-10-05", "2026-10-06", "2026-10-07", "2026-10-08", "2026-10-09", "2026-10-10", "2026-10-11"]
for day in days: 
    with open("C:/GIS/Data/AIS/processed/aisdk-" + day + "_box.csv", "r") as myfile, open("C:/GIS/Data/AIS/processed/aisdk-" + day + "_thin3.csv", "w", newline="") as outfile:
                reader = csv.reader(myfile)
                writer = csv.writer(outfile)
                headings = next(reader)
                writer.writerow(headings)
                total = 0
                ships = 0
                kept = 0
                seen = set()
                for row in reader:
                    total += 1
                    if row[1] == "Class A" or row[1] == "Class B":
                        ships += 1
                        hh = int(row[0][11:13])
                        mm = int(row[0][14:16])
                        slot = (hh * 60 + mm) // 3
                        key = (row[2], slot)
                        if key not in seen:
                            seen.add(key)
                            writer.writerow(row)
                            kept += 1
                print(day,total, ships, kept)
                    