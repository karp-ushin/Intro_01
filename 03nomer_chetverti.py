x = float(input("Введите 1-ю координату точки: "))
y = float(input("Введите 2-ю координату точки: "))
if x > 0:
    if y > 0:
        print("1-я четверть")
    else:
        print("4-я четверть")
else:
    if y > 0:
        print("2-я четверть")
    else:
        print("3-я четверть")
