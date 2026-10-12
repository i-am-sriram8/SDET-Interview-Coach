import re

text = "Case CASE-1042 created"
m = re.search(r"CASE-\d+", text)
case_id = m.group() if m else None

print(case_id)