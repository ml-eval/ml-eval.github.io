import csv
import sys
import datetime

path = sys.argv[1]

data = []
with open(path, "r") as f:
    csv_iter = iter(csv.reader(f))
    heading = next(csv_iter)
    for csv_line in csv_iter:
        row = dict(zip(heading, csv_line))
        if row["Session"] == "":
            break
        data.append(row)


with open("_data/schedule.csv", "w") as f:
    f.write("start,end,description\n")
    for line in data:
        start = list(map(int, line["Start (UTC)"].split(":")))
        start = datetime.datetime(
            year=2022, month=4, day=22, hour=start[0], minute=start[1]
        )
        duration = list(map(int, line["Duration"].split(":")))
        duration = datetime.timedelta(hours=duration[0], minutes=duration[1])
        end = start + duration
        description = line["Session"]
        f.write(
            ",".join([start.strftime("%Hh%M"), end.strftime("%Hh%M"), description])
            + "\n"
        )
