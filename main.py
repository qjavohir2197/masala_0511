#1-misol
import math
roy = [4, 9, 16, 25]
son = []

for i in roy:
    son.append(math.sqrt(i))
print(son)

#2-misol
numbers = [i for i in range(51) if i % 5 == 0]
print(numbers)

#3-misol
soz_roy =['hello', 'world', 'python']
katta_sozlar = []

for soz in soz_roy:
    katta_sozlar.append(soz.upper())
print(katta_sozlar)

#4-misol
words = ['car', 'bike', 'bus']
teskari_soz = []
for i in words:
    teskari_soz.append(i[::-1])
print(teskari_soz)

#5-misol
nums = [1, 2, 3, 4]
kvadrat_son = [n * 2 for n in nums]
print(kvadrat_son)
