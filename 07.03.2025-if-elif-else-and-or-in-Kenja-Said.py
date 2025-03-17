# Mavzu: if, elif, else, and, or, in
# sana:07.05.2025
# talaba = Kenjabek and Saidmuhammadxon


# if va else;
#
# x, y = 15, 25
# if x<y:
#     print("Y katta X dan")
# else:
#     print("Y katta X dan")

# if, elif, else:
#     if agar,
#     elif - agar, aks holda,
#     else aks holda


# yosh = int(input("Yoshingizni kiriting: "))
# if yosh>18:
#     print("Sizning kiritsh chiptangiz narxi 25000 so'm")
# elif yosh<18:
#     print("Sizning yoshingiz kichkina. Kirishga haqqingiz yo'q")

# and va degani
# or yoki degani

# yosh = int(input("Yoshingizni kiriting: "))
# if yosh>18 and yosh<60:
#     print("Sizning kiritsh chiptangiz narxi 25000 so'm")
# elif yosh<18:
#     print("Sizning yoshingiz kichkina. Kirishga haqqingiz yo'q")
# else:
#     print("Sizdek nuroniyni ko'rib turganimizdan xursandmiz. Sizga kirish mutlaqo bepul")

# or yoki

# kun = input("Bugungi kunni kiriting: ")
# harorat = float(input("Haroratni kiriting: ")) # +C yaxtaga -C uyda dam olamiz
# if (kun.lower()=="shanba" or kun.lower()=="yakshanba") and harorat>24:
#     print("Bugun dam olish kuni, Sayohatga boramiz")
# elif (kun.lower()=="shanba" or kun.lower()=="yakshanba") and harorat<24:
#     print("Bugun dam olish kuni, Lekin havo savuqligi sababli uyda o'tiramiz")
# else:
#     print("Bugun ish kuni. 9.00 dam 18.00 gacha ishda bo'lishing kerak")

# in - ichida

menu = ['osh', 'shashlik', 'manti', 'barak', 'kabob']

ovqat = input("Nima ovqat buyurasiz? ")
if ovqat.lower() in menu:
    print(f"{ovqat} menuda bor")
else:
    print(f"{ovqat} menuda yo'q")


menu = ['osh', 'shashlik', 'manti', 'barak', 'kabob']
taom = input("Yoqtirgan taomingizni kiriting: ")
buyurtmalar =[]
if taom in menu:
    buyurtmalar.append(taom)
    print(f"Buyurtma qabul qilindi")
else:
    print("Bu taom menuda yo'q")
print(f"Siz tanlagan taomlar {buyurtmalar}")

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