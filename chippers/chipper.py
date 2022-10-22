import xml.etree.ElementTree as ET

# Read problem definition
num_phrases = int(input())
num_xml_lines = int(input())
num_rows, num_cols = input().split(",")
num_cols = int(num_cols)
num_rows = int(num_rows)
match_first = input() == "S"
phrases = [input() for i in range(num_phrases)]

# Parse xml

max_i = num_rows * num_cols
col = 0
row = 1
chipper = {}

xml_raw = ""
for _ in range(num_xml_lines):
    xml_raw += input()
tree = ET.fromstring(xml_raw)
notags = ET.tostring(tree, encoding='utf8', method='text')
notags = notags.decode()
for char in notags:
    col += 1
    if col > num_cols:
        col = 1
        row += 1
    if row > num_rows:
        break
    if match_first:
        if not char in chipper:
            chipper[char] = f"{row},{col}"
    else:
        chipper[char] = f"{row},{col}"

for phrase in phrases:
    res = ""
    for character in phrase:
        if not character in chipper:
            res = "0,"
            break
        res += chipper[character]+","
    print(res[:-1])



