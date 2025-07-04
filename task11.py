'''11.Fayl mavjud bo‘lmasa yaratish
Tavsif: Dastur ishga tushganida students.json fayli mavjud bo‘lmasa, uni avtomatik yaratadigan kod yozing.
'''

import json
import os

if not os.path.exists("output"):
    os.mkdir("output")

if not os.path.exists("output/students.json"):
    with open("output/students.json", "w") as f:
        json.dump([], f,indent=4)
