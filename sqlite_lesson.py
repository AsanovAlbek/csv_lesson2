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

cursor.execute("SELECT COUNT(*) FROM Food WHERE price > ?", (100, ))
for food in cursor.fetchall():
    print(dict(food))

# Обновление данных
# cursor.execute("UPDATE Food SET price = price * 0.8 WHERE name = ?", ('Ростмастер', ))

# Удаление данных
cursor.execute("DELETE FROM Food WHERE name = ?", ('Наггетсы', ))
connection.commit()

# закрываем
cursor.close()
connection.close()

connection = sqlite3.connect("rostics.db")
connection.row_factory = sqlite3.Row # Настройка, чтобы select возвращал словарь
cursor = connection.cursor()

# Пример SQL - инъекции (никогда так не делайте!)
food_id = input("Введите id:")
# Попробуйте ввести 1 OR 1 = 1 и ВСЕ ВАШИ ДАННЫЕ УДАЛЯТСЯ!!!!!
cursor.execute(f"DELETE FROM Food WHERE id = {food_id}")
connection.commit()

# Транзакция
try:
    cursor.execute("INSERT OR IGNORE INTO Food(name, price) VALUES (?, ?)", ("Крылышки", 200)) # 1
    cursor.execute("UPDATE Food SET price = 150 WHERE name = ?", ("Крылышки",)) # 2
    # raise Exception("Хьюстон, у нас проблема")
    connection.commit()
except Exception as e:
    connection.rollback()
    print("Откат транзакции.", e)
finally:
    cursor.close()
    connection.close()

