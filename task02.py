'''2.JSON faylni o‘qish
Tavsif: Yuqoridagi students.json faylini o‘qing va har bir talabaning ismi bilan yoshi ekranga chiqsin:

Ali - 20 yosh
Laylo - 21 yosh
Bekzod - 19 yosh'''

import json

with open("output/students.json", "r") as f:
    students = json.load(f)

for student in students:
    text = student["name"] + " - " + str(student["age"]) + " yosh"
    print(text)
