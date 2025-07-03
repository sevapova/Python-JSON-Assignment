'''10. Tartiblab chiqish
Tavsif: Talabalarni yosh bo‘yicha oshib boruvchi tartibda chiqaring.
'''

import json

with open("output/students.json", "r", encoding="utf-8") as f:
    students = json.load(f)

sorted_students = sorted(students, key=lambda s: int(s["age"]))

for s in sorted_students:
    text = s["name"] + " - " + str(s["age"]) + " yosh"
    print(text)
