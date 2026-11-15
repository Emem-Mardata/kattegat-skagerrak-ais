import csv
import os
import sys

# Reads the RAW, unzipped day file, to check its structure before filtering.
# Pass a path as the first argument to inspect a different file.
BASE = os.environ.get("AIS_BASE", r"C:/GIS/Data/AIS")
DEFAULT = os.path.join(BASE, "raw", "aisdk-2026-10-12", "aisdk-2026-10-12.csv")
path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT

with open(path, "r") as myfile:
    count = 0
    for line in myfile:
        count = count + 1
        print(count, line.strip())
        if count == 5:
            break
