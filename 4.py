X,Y,N = map(int, input("Введите через пробел рубли, "
                       "копейки, количество заказов: ").split())
cop = X*100 + Y
income = cop*N
R = income // 100
K= income % 100
print("Доход за день:", R, 'руб.', K,'коп.')