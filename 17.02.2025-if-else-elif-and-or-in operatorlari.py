# Sana: 17.03.2025
# Mavzu:if-elif-else-and-or-in


# print("Sonni musbat yoki manfiyligini tekshirish uchun sonni kiriting:")
# son = int(input("Son: "))
# if son>0:
#     print("Musbat son")
# else:
#     print("Manfiy son")


# and -> va
# or -> yoki


# print("Bugun nima kun:")
# kun = input("Kunni kiriting: ")
# if kun.lower() == "shanba" or  kun.lower()=="yakshanba":
#     print("Bugun dam olish kuni")
# else:
#     print("Bugun ish va o'qish kuni. Darslaringni tayyorla")

# print("Dam olish yoki ish kuni")
# kun = input("Bugun kunni kiriting:")
# harorat = float(input("Haroratni kiting: "))
#
# if (kun.lower() == "shanba" or kun.lower() == "yakshanba") and harorat <= 15:
#     print("Bugun dam olish kuni lekin havo sovuq. Uyda o'tiramiz")
#
# elif (kun.lower() == "shanba" or kun.lower() == "yakshanba") and harorat >= 15:
#     print("Bugun dam olish kuni ketdik plyajga!! Do'stlarga tel qil!!!")
#
# else:
#     print("Bugun ish kuni soat 9:00 dan 18:00 gacha ishda bo'lish kerak")

# menu = ["osh", 'somsa', 'shashlik']
# print(menu)
# taom = input("Taom nomini kiriting: ")
# if taom in menu:
#     print("Bu taom mavjud")
# else:
#     print("Bu taom qolmagan")


# print((78-20)*3)
# print(78-20*3)


#Vazifa
"""> 1.Quyidagi dasturlarni alohida fayllarga yozing va bajaring:
>
>
> Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
>
> 2.Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepulAgar foydalanuvchi 18 dan kichik bo'lsa 10000 so'mAgar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
>
> Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
>
> `mahsulotlar` degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, `savat` degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, `mahsulotlar` ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "*Mahsulot* do'konimizda bor" aks holda, "*Mahsulot* do'konimizda yo'q" degan xabarlarni chiqaring.
>
> Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, `bor_mahsulotlar` degan ro'yxatga, do'konda yo'q mahsulotlarni esa `mavjud_emas` degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
>
> `foydalanuvchilar` degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, *foydalanuvchi*!" xabarini chiqaring.
>
> Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.
>"""

# mahsulotlar` degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting.
# Yangi, `savat` degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida
# 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, `mahsulotlar` ro'yxati
# bilan solishtiring va qaysi biri ro'yxatda bo'lsa "*Mahsulot* do'konimizda
# bor" aks holda, "*Mahsulot* do'konimizda yo'q" degan xabarlarni chiqaring.


mahsulotlar = ["non", "nok", "olma", "karam", "tuxum", "qovun", "tarvuz"]
savatlar = []
for n in range(5):
    savatlar.append(input(f"{n+1}- mahsulotni kiriting:"))
print(savatlar)

if savatlar:
    for savat in savatlar:
        if savat in mahsulotlar:
            print(f"Bu {savat} mahsuloti Magazinda mavjud")
        else:
            print(f"Bu {savat} mahsuloti Magazinda mavjud emas")















