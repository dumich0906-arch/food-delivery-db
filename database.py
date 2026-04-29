import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect('food_delivery.db')
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("DROP TABLE IF EXISTS customers")
cursor.execute("DROP TABLE IF EXISTS restaurants")

cursor.execute("""
CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE restaurants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    cuisine TEXT NOT NULL,
    rating REAL NOT NULL,
    address TEXT NOT NULL,
    phone TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    restaurant_id INTEGER NOT NULL,
    items TEXT NOT NULL,
    total_amount REAL NOT NULL,
    order_date TEXT NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
)
""")

first_names = ["Алексей", "Мария", "Иван", "Ольга", "Дмитрий", "Анна", "Сергей", 
               "Елена", "Андрей", "Татьяна", "Максим", "Светлана", "Николай", 
               "Екатерина", "Владимир", "Юлия", "Артём", "Наталья", "Павел", 
               "Ирина", "Константин", "Виктория", "Роман", "Алина", "Георгий", 
               "Полина", "Михаил", "Вероника", "Денис", "Ксения"]

last_names = ["Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов", "Попов", 
              "Васильев", "Соколов", "Михайлов", "Новиков", "Федоров", "Морозов", 
              "Волков", "Алексеев", "Лебедев", "Семенов", "Егоров", "Павлов", 
              "Козлов", "Степанов", "Николаев", "Орлов", "Андреев", "Макаров", 
              "Захаров", "Зайцев", "Соловьев", "Борисов", "Яковлев", "Григорьев"]

streets = ["Ленина", "Пушкина", "Гагарина", "Мира", "Советская", "Кирова", 
           "Энгельса", "Чехова", "Толстого", "Достоевского", "Горького", 
           "Фрунзе", "Калинина", "Свердлова", "Октябрьская", "Партизанская", 
           "Комсомольская", "Победы", "Строителей", "Юбилейная"]

restaurant_names = ["Пицца Рома", "Суши Мастер", "Бургер Кинг", "Шаурма №1", 
                    "Грузинский дворик", "Китайский дракон", "Мексикано", 
                    "Итальяно", "Стейк Хаус", "Вкусно и точка", "Кафе Уют", 
                    "Пельменная", "Кебаб Хаус", "Паста Фреш", "Ролл Сити", 
                    "Тандур", "Вок и Ролл", "Блинная", "Кофе и Точка", 
                    "Лаваш Бар", "Плов Центр", "Супер Суши", "Пицца Тайм", 
                    "Барбекю Шеф", "Фалафель Хаус", "Курица Гриль", 
                    "Паназиатика", "Европа Кафе", "Домашняя кухня", "Фастфуд 24"]

cuisines = ["Итальянская", "Японская", "Американская", "Восточная", "Грузинская", 
            "Китайская", "Мексиканская", "Русская", "Европейская", "Корейская"]

dishes_list = [
    "Пепперони, Кола", "Филадельфия, Мисо суп", "Воппер, Картофель фри", 
    "Шаурма классическая, Фанта", "Хачапури, Хинкали", "Лапша удон, Спринг-роллы",
    "Тако, Начос", "Паста Карбонара, Тирамису", "Рибай, Картофель по-деревенски",
    "Биг Мак, Наггетсы", "Борщ, Пирожки", "Пельмени со сметаной", 
    "Донер, Айран", "Феттучини, Брускетта", "Калифорния, Тунец", 
    "Плов, Шашлык", "Вок с курицей, Спринг-ролл", "Блины с икрой", 
    "Капучино, Круассан", "Лаваш с сыром", "Плов узбекский", 
    "Сет Филадельфия", "Маргарита, Цезарь", "Рёбра BBQ, Кукуруза", 
    "Фалафель, Хумус", "Куриные крылышки, Соус", "Рамен, Гедза", 
    "Стейк, Овощи гриль", "Котлеты с пюре", "Чизбургер, Молочный коктейль"
]

statuses = ["Доставлен", "В пути", "Готовится", "Отменён", "Ожидает"]

for i in range(30):
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    phone = f"+7(9{random.randint(10,99)}){random.randint(100,999)}-{random.randint(10,99)}-{random.randint(10,99)}"
    address = f"ул. {random.choice(streets)}, д. {random.randint(1,150)}, кв. {random.randint(1,300)}"
    cursor.execute("INSERT INTO customers (name, phone, address) VALUES (?, ?, ?)", 
                   (name, phone, address))

for i in range(30):
    name = restaurant_names[i]
    cuisine = random.choice(cuisines)
    rating = round(random.uniform(3.5, 5.0), 1)
    address = f"ул. {random.choice(streets)}, д. {random.randint(1,100)}"
    phone = f"+7(8{random.randint(10,99)}){random.randint(100,999)}-{random.randint(10,99)}-{random.randint(10,99)}"
    cursor.execute("INSERT INTO restaurants (name, cuisine, rating, address, phone) VALUES (?, ?, ?, ?, ?)", 
                   (name, cuisine, rating, address, phone))

for i in range(30):
    customer_id = random.randint(1, 30)
    restaurant_id = random.randint(1, 30)
    items = dishes_list[i]
    total_amount = round(random.uniform(300, 2500), 2)
    days_ago = random.randint(0, 90)
    order_date = (datetime.now() - timedelta(days=days_ago)).strftime("%Y-%m-%d %H:%M:%S")
    status = random.choice(statuses)
    
    cursor.execute("""
        INSERT INTO orders (customer_id, restaurant_id, items, total_amount, order_date, status) 
        VALUES (?, ?, ?, ?, ?, ?)
    """, (customer_id, restaurant_id, items, total_amount, order_date, status))

conn.commit()

print("Проверка данных:")
for table in ["customers", "restaurants", "orders"]:
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    print(f"Таблица '{table}': {count} записей")

conn.close()
print("База данных создана и заполнена.")