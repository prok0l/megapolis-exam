with open("astronaut_time.csv", encoding="utf-8") as f:
    """Считывание данных"""
    keys = f.readline().strip().split(',')
    data = list()  # список для хранения входных данных
    for line in f:
        values = [int(x) if x.isdigit() else x for x in line.strip().split(',')]
        data.append(dict(zip(keys, values)))


output_lines = list()  # список для хранения выходных данных
for item in data:
    time = item["timeStop"]
    hours, minutes, seconds = map(int, time.split(":"))
    hours = (hours + item["count"]) % 24
    timeNow = ":".join([str(x).zfill(2) for x in [hours, minutes, seconds]])  # создание строки с актуальным временем
    numberStation = item["numberStation"]
    cabinNumber = item["cabinNumber"]
    line = (f"На станции {numberStation} в каюте {cabinNumber} восстановлено время. "
            f"Актуальное время {timeNow}")  # создание строки
    output_lines.append(line)

with open("new_time.txt", "a+", encoding="utf-8") as f:
    """Запись данных в выходной файл"""
    f.writelines(output_lines)

print(*output_lines[:3], sep="\n")  # вывод первых 3х записей
