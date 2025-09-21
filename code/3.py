price=float(input("price: "))
discount=float(input("discount: "))
vat=float(input("vat: "))
baza=price*(1-discount/100)
nds=baza*(vat/100)
itog=baza+nds
print("База: "+(str(baza)))
print("НДС: "+(str(nds)))
print("Итог: "+(str(itog)))
