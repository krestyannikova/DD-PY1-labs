capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
# задаем переменную для количества месяцев
month = 0
# вводим условие, которое будет сравнивать траты с зарплатой
while True:
    delta = spend - salary
    if delta > capital:
        break
    # увеличиваем цены
    month += 1
    capital -= delta
    spend *= 1 + increase

print("Количество месяцев, которое можно протянуть без долгов:", month)

