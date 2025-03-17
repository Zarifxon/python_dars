# Sana: 12.02.2025
# Mavzu: For sikli bilan tanishamiz
# for -> uchun degani
# mehmonlar = ["Kamron", "Mashhurbek", "Kenjabek", "Islom"]
# # for mehmon in mehmonlar:
# #     # print("Salom ", mehmon)
# #     print("Xayr ", mehmon)
#
# for mehmon in mehmonlar:
#     print(f"Assalomu alaykum {mehmon}! \nSizni 18 noyabrda bizning uyda mehmon bo'lishizni so'rayman")
#
# sonlar= [1, 2, 3, 4, ... ,14]

sonlar=list(range(1,15))
for son in sonlar:
  print(f"{son} ning kvadrati {son**2} ga teng")

# ifoda = list(range(a, b, c))

# a = start(boshlanish sonlari)
# b = stop(Tugashi)
# c = step(Qadam)

# sonlar = list(range(1, 99, 2))
#
# for son in sonlar:
#     print(f" {son}ning kubi {son**3}ga teng")

kinolar = []
s = []
print('Yoqtirgan kinolaraingizni sonini kiriting!!!')
s = int(input("Soni: "))
for n in range(s):
    kinolar.append(input(f"{n+1}- kinoni nomini kiriting: "))
print(f"Siz yoqtirgan kinolar soni {s} ta,"
      f" ularning nomlari {kinolar}")












# kinolar = []
# print("Sizga yoqgan 5 ta kino nomini kiriting: ")
# for n in range(5):
#   kinolar.append(input(f"{n+1}- kinoni nomini kiriting: \n"))
# print(f"Siz yoqtirgan kinolar ro'yxati {kinolar}")

# uchratganlar = []
# # s = []
# print("Bugun ushrtagan kishilar sonini kiriting: ")
# s = int(input("Soni: "))
# for n in range(s):
#     uchratganlar.append(input(f"{n+1}- Kishini ismini kiriting: "))
# print(f"Siz bugun uchratkan kishilar soni {s} ta  va ularning ismlari: ",  uchratganlar)