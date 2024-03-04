import math
def calculate_angles(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Некорректные значения сторон треугольника"

    if a + b <= c or a + c <= b or b + c <= a:
        return "Треугольник с такими сторонами не существует"

    alpha = math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))
    beta = math.degrees(math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))
    gamma = math.degrees(math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)))

    return alpha, beta, gamma

a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

angles = calculate_angles(a, b, c)

if angles:
    print(f"Значение угла 1: {angles[0]}°")
    print(f"Значение угла 2: {angles[1]}°")
    print(f"Значение угла 3: {angles[2]}°")