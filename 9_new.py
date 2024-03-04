def passer_rating(att, comp, yds, td, int):

    a = max(0, min((comp / att - 0.3) * 5, 2.375))
    b = max(0, min((yds / att - 3) * 0.25, 2.375))
    c = max(0, min((td / att) * 20, 2.375))
    d = max(0, min(2.375 - (int / att * 25), 2.375))

    pass_rating = (a + b + c + d) / 6 * 100
    return pass_rating

att = float(input("Введите количество попыток передач (ATT): "))
comp = float(input("Введите количество успешных передач (COMP): "))
yds = float(input("Введите общее количество ярдов по передачам (YDS): "))
td = float(input("Введите количество передач, завершенных тачдаунами (TD): "))
int = float(input("Введите количество перехваченных передач (INT): "))


pass_rating = passer_rating(att, comp, yds, td, int)


print(f"Passer rating игрока: {pass_rating:.1f}")