import re

l = "better"

matches = re.findall("better", l, re.IGNORECASE)

print(matches)
