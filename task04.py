'''4. Foydalanuvchidan ma’lumot olib JSON ga yozish
Tavsif: input() yordamida foydalanuvchidan ism, familiya, yosh so‘rang va mavjud students.json fayliga qo‘shib yozing.

'''

import json 

with open("output/students.json", "r") as f:
     students = json.load(f)


name = input("Ismingizni kiriting: ")
surname = input("Familyangizni kiriting: ")
age = int(input("Yoshingizni kiriting: "))

new_student = {
     "name" : name,
     "surname" : surname,
     "age" : age
}
students.append(new_student)

with open("output/students.json", 'w') as f:
     json.dump(students,f, indent=4)

print("Malumot qoshildi!")
