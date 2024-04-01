with open("astronaut_time.csv", encoding="utf-8") as f:
    """Считывание данных"""
    keys = f.readline().strip().split(",")
    data = list()  # список для хранения входных данных

    for line in f:
        values = [int(x) if x.isdigit() else x for x in line.strip().split(",")]
        data.append(dict(zip(keys, values)))


while (input_str := input()) != "stop":
    """Запрос номера станции у пользователя"""
    for item in data:
        """Поиск данных в исходном файле"""
        if item["numberStation"] == input_str:
            numberStation = item["numberStation"]
            timeStop = item["timeStop"]

            time = item["timeStop"]
            hours, minutes, seconds = map(int, time.split(":"))
            hours = (hours + item["count"]) % 24
            timeNow = ":".join(
                [str(x).zfill(2) for x in [hours, minutes, seconds]])  # создание строки с актуальным временем

            line = (f"На станции {numberStation} восстановлено время (время остановки: {timeStop}). "
                    f"Актуальное время {timeNow}")  # создание строки
            print(line)
            break
    else:
        print("На этой станции все хорошо")  # обработка отсутствия станции в файле
