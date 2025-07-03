'''7. Statistika chiqarish
Tavsif: students.json faylidan o‘rtacha yoshni hisoblang.'''

import json


with open("output/students.json", "r") as f:
    students = json.load(f)

age = [int(s["age"]) for s in students]

avg = sum(age) /len(age)

print("O'rtacha yosh:", avg)