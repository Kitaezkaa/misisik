# Лабораторная работа 1
## Задание 1
![name=input()
age=int(input())
print("Привет,"+name+" через год тебе будет "+(str((age+1))))
](./images/01.png) 
## Задание 2
![a=input("a: ").replace(",",".")
b=input("b: ").replace(",",".")
a=float(a)
b=float(b)
s=a+b
avg=s/2
print(s,avg)](./images/02.png)
## Задание 3
![price=float(input("price: "))
discount=float(input("discount: "))
vat=float(input("vat: "))
baza=price*(1-discount/100)
nds=baza*(vat/100)
itog=baza+nds
print("База: "+(str(baza)))
print("НДС: "+(str(nds)))
print("Итог: "+(str(itog)))](./images/03.png)
## Задание 4
![m=int(input())
ch=m//60
mm=m%60
print(ch,":",mm)](./images/04.png)
## Задание 5
![fio=input("ФИО: ")
fio_stripped=fio.strip()
length=len(fio_stripped)
fio_pr=fio_stripped.split()
initials=''.join([word[0].upper() for word in fio_pr])
print("Инициалы: ",initials)
print("Длина: ",length)](./images/05.png)