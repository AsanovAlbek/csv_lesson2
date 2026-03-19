import csv
import json

FILENAME = "clients.csv"

"""Функция для миграции csv в json"""
def export_to_json(json_file_name: str, csv_file_name: str, fields: list[str]):
    data = []
    with open(csv_file_name, "r", newline="") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";", fieldnames=fields)
        next(reader)
        for row in reader:
            data.append(row)

    with open(json_file_name, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


clients = [
    { "имя" : "Артур", "возраст" : 24, "номер телефона" : "+7 (933) 333 33 33" },
    { "имя" : "Адам", "возраст": 17, "номер телефона" : "+7 (938) 917 32 27" },
    { "имя" : "Влад", "возраст" : 18, "номер телефона" : "+7 (938) 079 47 94" },
]

with open(FILENAME, "w", newline="") as file:
    fields = ["имя", "возраст", "номер телефона"]
    writer = csv.DictWriter(file, delimiter=";", fieldnames=fields)
    writer.writeheader()
    writer.writerows(clients)

export_to_json("clients.json", "clients.csv", fields)

with open(FILENAME, "r", newline="") as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        print(f"Имя: {row["имя"]}, телефон: {row["номер телефона"]}")