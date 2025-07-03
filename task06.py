'''6. JSONdan boshqa CSV formatga o‘tkazish
Tavsif: students.json faylini students.csv fayliga aylantiring. Har bir qatorda ism, familiya, yosh bo‘lsin.

'''

import json
import csv

with open("output/students.json", "r") as f:
    students = json.load(f)

with open("output/students.csv", "w") as f:
    writer = csv.writer(f)
    
    writer.writerow(["name", "surname", "age"])
    
    for s in students:
        writer.writerow([s["name"], s["surname"], s["age"]])
