import sqlite3
'''
CREATE TABLE countries (
    id INT PRIMARY KEY AUTO_INCREMENT,title VARCHAR(255) NOT NULL
);'''

'''INSERT INTO countries (title) VALUES ('Russia'),('USA'),('Germany');'''
'''CREATE TABLE cities (
id INT PRIMARY KEY AUTO_INCREMENT, title VARCHAR(255) NOT NULL, area DECIMAL(10,2) DEFAULT 0,
country_id INT, FOREIGN KEY (country_id) REFERENCES countries (id));'''

'''INSERT INTO cities (title,country_id) VALUES 
('Moscow',1),
('Paris',2),
('NY',3),
('London',1),
('Washington',2),
('Berlin',3),
('Bishkek',1)'''

'''CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    city_id INT,
    FOREIGN KEY (city_id) REFERENCES cities(id)
)'''

'''INSERT INTO students (first_name, last_name, city_id) VALUES
('Иван', 'Петров', 1),
('Мария', 'Иванова', 2),
('Алексей', 'Сидоров', 3),
('Елена', 'Козлова', 4),
('Павел', 'Смирнов', 5),
('Ольга', 'Николаева', 6),
('Дмитрий', 'Кузнецов', 7),
('Анна', 'Павлова', 1),
('Сергей', 'Морозов', 2),
('Юлия', 'Красавина', 3),
('Артем', 'Захаров', 4),
('Екатерина', 'Белова', 5),
('Игорь', 'Денисов', 6),
('Виктория', 'Соловьева', 7),
('Даниил', 'Комаров', 1);'''

def display_cities(connection):
    try:
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, title FROM cities")
        cities = cursor.fetchall()
        return cities
    except sqlite3.Error as error:
        print(error)
        return []

def display_students_by_city(city_id):
    try:
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area "
                   "FROM students "
                   "JOIN cities ON students.city_id = cities.id "
                   "JOIN countries ON cities.country_id = countries.id "
                   "WHERE cities.id = ?", (city_id,))
        students = cursor.fetchall()
        return students
    except sqlite3.Error as error:
        print(error)
        return []


    for student in students:
        print(f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь города: {student[4]}")

while True:
    display_cities(connection=1)
    city_id = int(input("Введите id города для отображения учеников (для выхода введите 0): "))
    if city_id == 0:
        break
    else:
        display_students_by_city(city_id)

connection.close()