
# Задание 1

print("Vvedite chislo")
chislo=int(input())
if   chislo %2==0 and chislo < 0:
    print("Chislo chetnoe-otrits")
elif  chislo %2!=0 and chislo < 0:
    print("Chislo nechetnoe-otrits")
elif  chislo %2==0 and chislo > 0:
    print("Chislo chetnoe-polozhit")
elif  chislo %2!=0 and chislo > 0:
    print("Chislo nechetnoe-polozhit")
else :
    print("Chislo = 0")