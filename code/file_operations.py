import json
import csv

# with open("sample.json") as f:
#     data = json.load(f)

# body = response.json()
# assert body["status"] == "open"
# case_id = body.get("case_id")

with open("basic-data.csv", newline="") as f:
        rows = list(csv.DictReader(f))
        print(rows[1:5])