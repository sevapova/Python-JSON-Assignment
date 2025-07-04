'''1.Ma’lumotni JSON faylga yozish
Tavsif: Talabalar ro‘yxati bor (ism, familiya, yosh). Shu ma’lumotlarni students.json faylga yozing.

# Ma’lumotlar:
students = [
    {"name": "Ali", "surname": "Valiyev", "age": 20},
    {"name": "Laylo", "surname": "Karimova", "age": 21},
    {"name": "Bekzod", "surname": "Xolmatov", "age": 19}
]'''

import json
import os

if not os.path.exists("output"):
    os.mkdir("output")

students = [
    {"name": "Ali", "surname": "Valiyev", "age": 20},
    {"name": "Laylo", "surname": "Karimova", "age": 21},
    {"name": "Bekzod", "surname": "Xolmatov", "age": 19}
]

with open('output/students.json', 'w') as jsonf:
    json.dump(students,jsonf, indent=4)