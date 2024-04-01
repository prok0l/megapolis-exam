with open("astronaut_time.csv", encoding="utf-8") as f:
    """Считывание данных"""
    keys = f.readline().strip().split(",")
    data = list()  # список для хранения входных данных

    for line in f:
        values = [int(x) if x.isdigit() else x for x in line.strip().split(",")]
        data.append(dict(zip(keys, values)))


list_stop = list()
for item in data:
    """Поиск станций с временем простоя 9"""
    if item['count'] == 9:
        numberStation = item["numberStation"]
        count = item["count"]
        list_stop.append(map(str, (numberStation, count)))
        print(numberStation, count)


output_lines = [" ".join(x) for x in list_stop]  # формирование выходных строк
with open("station_max_downtime.csv", "a+", encoding="utf-8") as f:
    """Запись данных в выходной файл"""
    f.write("\n".join(output_lines))
