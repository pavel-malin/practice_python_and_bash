import re

string = "Three the"

m = re.findall("Th[re]e", string, re.IGNORECASE)

print(m)
