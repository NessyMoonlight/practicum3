seconds = int(input("Введите время в секундах:"))
hours = seconds // 3600
remains = seconds % 3600
minutes = remains // 60
sec = remains % 60
print(hours,'часов',minutes,'минут',sec,'секунд')