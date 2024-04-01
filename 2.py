with open("astronaut_time.csv", encoding="utf-8") as f:
    """Считывание данных"""
    keys = f.readline().strip().split(",")
    data = list()  # список для хранения входных данных
    for line in f:
        values = [int(x) if x.isdigit() else x for x in line.strip().split(",")]
        data.append(dict(zip(keys, values)))


for j in range(1, len(data)):
    """Сортировка вставками полученных данных"""
    value = data[j]
    i = j - 1
    while i >= 0 and value["cabinNumber"].split("-")[1] < data[i]["cabinNumber"].split("-")[1]:
        data[i + 1] = data[i]
        i -= 1
    data[i + 1] = value

for ind in range(3):
    """Вывод 3х первых станций"""
    time = data[ind]["timeStop"]
    hours, minutes, seconds = map(int, time.split(":"))
    hours = (hours + data[ind]["count"]) % 24
    timeNow = ":".join([str(x).zfill(2) for x in [hours, minutes, seconds]])  # создание строки с актуальным временем
    numberStation = data[ind]["numberStation"]
    cabinNumber = data[ind]["cabinNumber"]
    line = (f"На станции {numberStation} в каюте {cabinNumber} восстановлено время. "
            f"Актуальное время {timeNow}")  # формирование выходной строки
    print(line)
