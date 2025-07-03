'''5. Yosh bo‘yicha filtr qilish
Tavsif: students.json faylidan faqat 20 yoshdan katta bo‘lganlarni ekranga chiqaring.

'''

import json

with open("output/students.json", "r") as f:
    students = json.load(f)

filtered = filter(lambda x: int(x["age"]) > 20, students)

for s in filtered:
    text = s["name"] + " - " + str(s["age"]) + " yosh"
    print(text)
