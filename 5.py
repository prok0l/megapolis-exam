with open("astronaut_time.csv", encoding="utf-8") as f:
    """Считывание данных"""
    keys = f.readline().strip().split(",")
    stations = dict()  # хэш таблица для хранения входных данных

    for line in f:
        values = [int(x) if x.isdigit() else x for x in line.strip().split(",")]
        d = dict(zip(keys, values))
        key = d['numberStation'].split('-')[0]
        stations[key] = stations.get(key, []) + [d]  # добавление астронавта в соответствующую группу

for group_number in stations.keys():
    """Вывод данных по каждой группе"""
    cabins = ", ".join([x['cabinNumber'] for x in stations[group_number]])
    downtimes = [x['count'] for x in stations[group_number]]
    average_downtime = str(sum(downtimes) / len(downtimes)).replace('.', ',')  # опреление ср. времени простоя
    print(f"Номер группы: {group_number}. Каюты: {cabins}. Время простоя: {average_downtime}")
