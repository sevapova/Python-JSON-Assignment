'''8. Top Student (Maksimal yosh)
Tavsif: Eng katta yoshli talabani toping va chiqaring.

'''

import json

with open("output/students.json", "r") as f:
    students = json.load(f)

student = max(students, key=lambda s: int(s["age"]))

text = student["name"] + "-" + str(student["age"]) + "yosh"

print(text)