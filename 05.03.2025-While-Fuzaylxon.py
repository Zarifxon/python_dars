#mavzu While operatori
# sana 05.03.2025

# son = 1
# while son <=5:
#     print(son, end=" ")
#     # son = son+1
#     son +=1
# print("Dastur tugatildi")

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan sonni kiriting "
# savol += "(Dasturni to'xtatish uchun 'exit' deb yozing):"
# qiymat = ""
# while qiymat != "exit":
#   qiymat = input(savol)
#   if qiymat != "exit":
#       print(float(qiymat)**2)
#
# print("Dastur tugadi. Rahmat!!!")



# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan sonni kiriting "
# savol += "(Dasturni to'xtatish uchun 'exit' deb yozing):"
#
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat =='exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
#
# print("Dastur tugatildi rahmat!!!")


# break to'xtatmoq, yakunlamoq
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan sonni kiriting "
# savol += "(Dasturni to'xtatish uchun 'exit' deb yozing):"


# while True:
#     qiymat = input(savol)
#     if qiymat =='exit':
#         break
#     else:
#         print(float(qiymat)**2)
#
# print("Dastur tugatildi rahmat!!!")


# sonlar =list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     else:
#         print(f"{son} ning kubi {son**3} ga teng")

"""Vazifa"""
"""1.Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. 
Foydalanuvchi `stop` so'zini yozishi bilan dasturni to'xtating
> 

> 2.Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 
7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 
18-65 gacha 10000 so'm, 65 dan kattalarga bepul. 
Shunday while tsikl yozingki, dastur foydalanuvchi 
yoshini so'rasin va chipta narhini chiqarsin. 
Foydalanuvchi `exit` yoki `quit` deb yozganda dastur to'xtasin 
(ikkita shartni ham tekshiring). 1.Yuqoridagi dasturni turli 
usullarda yozib ko'ring (break, ishora, yoki shart tekshirish)
>"""
# 1-qism
# 2-qism keyingi darsda
# 07.03.2025
# Mavzu: while davomi


# continue berilgan shartda o'sha shartni tashlab o'tadi
# sonlar =list(range(1,11))
# for son in sonlar:
#     if son==5:
#         continue
#     else:
#         print(f"{son} ning kvadrati {son**2} ga teng")

# son = 0
# while son<10:
#     son+=1
#     if son%2!=0:
#         continue
#     else:
#         print(son)


son = 0
while son>0:

    if son%2!=0:
        continue
    else:
       print(son)
       son += 1

"""Vazifa"""
"""
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat<0:
        continue
    elif qiymat=='Exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
        """