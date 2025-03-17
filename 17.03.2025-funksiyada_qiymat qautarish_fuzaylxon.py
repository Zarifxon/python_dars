# Mavzu: Funksiyada qiymat qaytarish
# sana:17.03.2025


# funksiydan log'at qaytarish ---------------------------------------- mavzucha

# def avto_info(kompaniya, model, rangi, karobka, yili, narhi = None):
#     avto = {
#         'kompaniya':kompaniya,
#         'model': model,
#         'rangi': rangi,
#         'karobka': karobka,
#         'yili': yili,
#         'narhi':narhi
#     }
#
#     return avto

#
# print("Online do'kanimizdagi mashinalar:")
#
# for avto in avtolar:
#     if avto['narhi']:
#         narh = avto['narhi']
#     else:
#         narhi="Nomalum"
#
#     print(f"Mashina modeli: {avto['model']} "
#           f"Rangi:{avto['rangi']} "
#           f"karobkasi: {avto['karobka']}"
#           f" Ishlab chiqarilgan yili: {avto['yili']}"
#           f" Narhi: {avto['narhi']}$")





# funkisyadan ro'yxat qaytarish----------------------mavzucha

# def oraliq(min, max):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min+=1
#     return sonlar
#
# print(oraliq(5, 10))
# print(oraliq(17,7))


# funksiyad sikl ishlashi takrorlanish----------------------------mavzucha
def avto_info(kompaniya=None, model=None, rangi=None, karobka=None, yili=None, narhi = None):
    avto = {
        'kompaniya':kompaniya,
        'model': model,
        'rangi': rangi,
        'karobka': karobka,
        'yili': yili,
        'narhi':narhi
    }

    return avto

# print("Saytimizdagi mashinalar ro'yxati--->>>")
cars = []

while True:
    print("Quyidagi ma'lumotlarni kiting\n",  end='' )
    kompaniya=input("Ishlab chiqaruvchini kiriting: ")
    model = input("Modelini kiriting: ")
    rangi = input("Rangini kiriting: ")
    karobka = input("Karobkasini kiriting: ")
    yili = input("Ishlab chiqarilgan yilini kiriting: ")
    narhi = input("narhini kiriting: ")

    cars.append(avto_info(kompaniya, model, rangi, karobka, yili, narhi))

    javob = input("Yana avto qo'shasizmi: (Y/N) ")
    if javob=="N":
        break


for car in cars:
    print(f" Ishlab chiqarilgan kompaniyasi {car['kompaniya']}"
          f" modeli: {car['model']} \n"
          f" rangi: {car['rangi']} \n"
          f" karobkasi: {car['karobka']}\n"
          f" ishlab chiqarilgan yili: {car['yili']}\n"
          f" narhi: {car['narhi']}"
          )

# print(cars)

# avto1 = avto_info("GM", "cobalt", "oq", "avtomat", "2024", "14000")
# avto2 = avto_info("BMW", "MBW X-5", "Qora", "Mexanika", "2025", "60000")
#
# avtolar = [avto1, avto2, ]


"""1.Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)

2.Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.

3.Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing.

4.Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing

5.Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)"""