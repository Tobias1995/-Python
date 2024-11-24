print("skolko deneg u Mihaila ?")
michael=int(input())
print("skolko deneg u Ivana ?")
ivan=int(input())
print("Kakaya summa investitsiy")
investition=int(input())
if michael>investition:
    print("Michael investor")
elif ivan>investition:
    print("Ivan investor")
elif ivan+michael>=investition:
    print(" vmeste Michael i Ivan investors")
elif ivan+michael<investition:
    print("nikto ne investor")
