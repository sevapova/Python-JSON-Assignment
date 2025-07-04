'''3.3. Yangi element qo‘shish
Tavsif: students.json fayliga yangi talaba qo‘shing:

{"name": "Shahzoda", "surname": "Nazarova", "age": 22}
'''

import json

with open("output/students.json", "r") as f:
     students = json.load(f)

x = {"name": "Shahzoda", "surname": "Nazarova", "age": 22}
students.append(x)


with open("output/students.json", 'w') as f:
     json.dump(students,f, indent=4)