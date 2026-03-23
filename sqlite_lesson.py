import sqlite3
# открываем соединение и курсор
# Если rostics.db нет, файл создаётся автоматически

connection = sqlite3.connect("rostics.db")
connection.row_factory = sqlite3.Row # Настройка, чтобы select возвращал словарь
cursor = connection.cursor()

# Создание таблицы
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Food(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        price REAL NOT NULL
    );
""")
# CRUD
# (Create (Создание) - Read (Чтение) - Update(Обновление) - Delete(Удаление))
# Запись данных
name = "Ростмастер"
price = 299.99
cursor.execute(f"INSERT OR IGNORE INTO Food(name, price) VALUES (?, ?);", (name, price))

food_list = [('Картошка', 100), ('Наггетсы', 80), ('Стрипсы', 150)]
cursor.executemany(f"INSERT OR IGNORE INTO Food(name, price) VALUES (?, ?);", food_list)
connection.commit()

# Получение данных
cursor.execute("SELECT * FROM Food WHERE price > ?", (100, ))
for food in cursor.fetchall():
    print(dict(food))

# закрываем
cursor.close()
connection.close()