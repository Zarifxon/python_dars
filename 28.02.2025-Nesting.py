# Mavzu: Nesting
# sana:28.02.2025


car0 ={
    "model": "nexia",
    "color" :" oq",
    "yil": "2015",
    "narh": 3000,
    "km": 400000,
    "karobka": "mexanika"
}
car1 ={
    "model": "malibu",
    "color" :"qora",
    "yil": "2025",
    "narh": 25000,
    "km": 0,
    "karobka": "avtomat"
}

car2 ={
    "model": "captiva",
    "color" :"GK2",
    "yil": "2020",
    "narh": 18000,
    "km": 300000,
    "karobka": "mexanika"
}

car3 ={
    "model": "ki",
    "color" :"mokriy",
    "yil": "2024",
    "narh": 60000,
    "km": 20000,
    "karobka": "avtomat"
}

car = car0

# print(f"Avtomobil haqidagi ma'umot!!! \n"
#       f"Model {car['model'].title() } \
#       rang:{car['color']} Chiqarilgan yil {car['yil']}, \
#       Narhi: {car['narh']}$, Yurgan masofa: {car['km']} \
#       karobkasi: {car['karobka']}")
#
# car = car1
# print(f"Avtomobil haqidagi ma'umot!!! \n"
#       f"Model {car['model'].title() } \
#       rang:{car['color']} Chiqarilgan yil {car['yil']}, \
#       Narhi: {car['narh']}$, Yurgan masofa: {car['km']} \
#       karobkasi: {car['karobka']}")

# cars = [car0, car1, car2, car3]
# for car in cars:
#     print(f"Avtomobil haqidagi ma'umot!!! \n"
#           f"Model {car['model'].title()} \
#           rang:{car['color']} Chiqarilgan yil {car['yil']}, \
#           Narhi: {car['narh']}$, Yurgan masofa: {car['km']} \
#           karobkasi: {car['karobka']}")


# lo'gat ichida ro'yxat
# dasturchilar = {
#     "ali" : ["python", "c++"],
#     "Fuzaylxon": ["python"],
#     "Lazizbek": ["kompsavodxon", 'python'],
#     "mashhurbek": ['python', 'django']
# }

# for ism, tillar in dasturchilar.items():
#     print(f"\n {ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())

# Vazifa
"""1. Talaba ma’lumotlarini chiqarish
Quyidagi talabalar ma’lumotlari berilgan:


talabalar = {
    "Ali": {"kurs": 2, "yosh": 20, "baholar": {"matematika": 5, "fizika": 4}},
    "Vali": {"kurs": 3, "yosh": 21, "baholar": {"matematika": 4, "fizika": 5}},
    "Hasan": {"kurs": 1, "yosh": 19, "baholar": {"matematika": 3, "fizika": 4}}
}
✔ Har bir talabaning kursi, yoshi va matematika bahosini ekranga chiqaring."""

"""2. Do‘kondagi mahsulotlar narxini hisoblash
Quyidagi mahsulotlar va ularning narxlari va miqdorlari berilgan:


do‘kon = {
    "olma": {"narx": 12000, "miqdor": 10},
    "banan": {"narx": 18000, "miqdor": 5},
    "uzum": {"narx": 25000, "miqdor": 8}
}
✔ Har bir mahsulotning umumiy narxini (narx × miqdor) hisoblab, ekranga chiqaring."""

"""3. Sport klubi ma’lumotlarini chiqarish
Quyidagi sport klubi a’zolarining yoshi va qaysi sport bilan shug‘ullanishi berilgan:


sport_klubi = {
    "Ali": {"yosh": 15, "sport": "Futbol"},
    "Vali": {"yosh": 17, "sport": "Basketbol"},
    "Hasan": {"yosh": 16, "sport": "Shaxmat"}
}
✔ Har bir a’zoning ismi, yoshi va sport turi bo‘yicha ma’lumot chiqaring."""

"""4. Maktabdagi sinflar va o‘quvchilar
Quyidagi sinflar va ularning o‘quvchilari berilgan:


maktab = {
    "1-A": {"o‘qituvchi": "Olimov", "o‘quvchilar": ["Ali", "Vali", "Hasan"]},
    "1-B": {"o‘qituvchi": "Karimova", "o‘quvchilar": ["Anvar", "Sardor", "Gulnoza"]}
}
✔ Har bir sinfning o‘qituvchisi va o‘quvchilari ro‘yxatini ekranga chiqaring."""

"""5. Kompaniya xodimlari va ularning lavozimlari
Quyidagi kompaniya xodimlari haqida ma’lumotlar berilgan:


kompaniya = {
    "Dasturchilar": {"Ali": "Backend", "Vali": "Frontend"},
    "Menejerlar": {"Hasan": "Loyiha boshqaruvi", "Sardor": "Marketing"}
}
✔ Har bir bo‘limdagi xodimlarning ismi va lavozimi bo‘yicha ma’lumot chiqaring."""


talabalar = {
    "Ali": {"kurs": 2, "yosh": 20, "baholar": {"matematika": 5, "fizika": 4}},
    "Vali": {"kurs": 3, "yosh": 21, "baholar": {"matematika": 4, "fizika": 5}},
    "Hasan": {"kurs": 1, "yosh": 19, "baholar": {"matematika": 3, "fizika": 4}}
}

"""Har bir talabaning kursi, yoshi va matematika bahosini ekranga chiqaring."""
for ism, info in talabalar.items():
    kurs = info['kurs']
    yosh = info['yosh']
    matem_baho = info['baholar']['matematika']
    print(f"Talabaning ismi {ism}, Yoshi {yosh}, talabaning o'qish kursi {kurs}, talabaning matematika faniadn bahosi {matem_baho}")




