seconds = int(input("Введите время в секундах:"))
hours = seconds // 3600
A = seconds % 3600
minutes = A // 60
sec = A % 60
print("Текущее время:",hours,'часов',minutes,'минут',sec,'секунд')