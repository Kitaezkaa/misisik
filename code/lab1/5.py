##Задание 5
fio=input("ФИО: ")
fio_stripped=fio.strip()
length=len(fio_stripped)
fio_pr=fio_stripped.split()
initials=''.join([word[0].upper() for word in fio_pr])
print("Инициалы: ",initials)
print("Длина: ",length)