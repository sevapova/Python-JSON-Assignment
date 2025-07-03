'''9. Studentlar sonini hisoblash
Tavsif: students.json faylidagi talabalarning umumiy sonini aniqlang.

'''

import json

with open("output/students.json", "r") as f:
    students = json.load(f)

count = len(students)

print(f"Talabalar soni: {count} ta")
