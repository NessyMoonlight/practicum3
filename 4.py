X,Y,N = map(int, input("Введите через пробел рубли,копейки,кол-во заказов: ").split())
cop = X*100 + Y
income = cop*N
rub = income // 100
cop2 = income % 100
print("Доход за день:",rub,'руб.',cop2,'коп.')