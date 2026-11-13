myfile = open("C:/GIS/Data/AIS/processed/aisdk-2026-10-12_box.csv", "r")
count = 0  # the counter starts at 0
for line in myfile:
    count = count + 1
    print(count, line.strip())
    if count == 5:
        break
myfile.close()
   