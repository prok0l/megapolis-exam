# 1. Название проекта: Набор программ для обработки csv файла с информацией о космических станциях

## 2. Описание проекта: Проет позволяет определять актуальное время на станциях, искать станции с большим временем простоя и группировать астронавтов по группам

## 3. Оглавление
 - [Название прокта](#1-название-проекта-набор-программ-для-обработки-csv-файла-с-информацией-о-космических-станциях)
 - [Описание проекта](#2-описание-проекта-проет-позволяет-определять-актуальное-время-на-станциях-искать-станции-с-большим-временем-простоя-и-группировать-астронавтов-по-группам)
 - [Оглавление](#3-оглавление)
 - [Как установить](#4-установка-продукта)
 - [Как запустить](#4-запуск-продукта)
 - [Как использовать проект](#5-как-использовать-проект)

### 4. Установка продукта

```shell
    git clone https://github.com/prok0l/megapolis-exam
```

### 4. Запуск продукта

- #### Linux
```shell
    python -m virtualenv venv
    source venv/Scripts/activate
    python3 1.py
    python3 2.py
    python3 3.py
    python3 4.py
    python3 5.py
    
```

- #### Windows
```shell
    python -m virtualenv venv
    .\venv\Scripts\activate
    python 1.py
    python 2.py
    python 3.py
    python 4.py
    python 5.py
```


### 5. Как использовать проект
- Проект позволяет анализировать входные данные. Для анализа ваших данных создайте файл astronaut_time.csv со следующими
  столбцами: WatchNumber, numberStation, cabinNumber, timeStop, count. 