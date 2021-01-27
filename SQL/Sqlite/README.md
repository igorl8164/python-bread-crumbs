### SQLite - python

execute(SQL)  SQL (Structured Query Language)

[DB Browser for SQLite ](https://sqlitebrowser.org?target=_blank)

Расширения файла базы данных SQLite \
*.db, *.db3, *.sqlite и *.sqlite3

---
## Типы данных SQLite
- NULL – значение NULL;
- INTEGER – целочисленный тип (занимает от 1 до 8 байт);
- REAL – вещественный тип (8 байт в формате IEEE);
- TEXT – строковый тип (в кодировке данных базы, обычно UTF-8);
- BLOB (двоичные данные, хранятся «как есть», например, для небольших изображений).


### Открыть / создать БД

``` python
import sqlite3 as sq

con = sq.connect("saper.db")
cur = con.cursor()

cur.execute("""
""")

con.close()

# менеджер контекста
with sq.connect("saper.db") as con:
    cur = con.cursor()
    cur.execute("""
    """)

```

### Создать таблицу
``` sh
cur.execute("""CREATE TABLE users (
    name TEXT,
    sex INTEGER,
    old INTEGER,
    score INTEGER
)""")

# создать если не существует

cur.execute("""CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    sex INTEGER,
    old INTEGER,
    score INTEGER
    )""")

```

### Выбор данных
```
# все поля
SELECT * FROM users


# скрытое поле rowid - уникальный идентификатор записи
SELECT rowid, * FROM users

```

### Удалить таблицу

```
cur.execute("DROP TABLE users")
# or
cur.execute("DROP TABLE IF EXISTS users")
```

### PRIMARY KEY, AUTOINCREMENT, NOT NULL и DEFAULT

```
cur.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT
    name TEXT NOT NULL,
    sex INTEGER NOT NULL DEFAULT 1,
    old INTEGER,
    score INTEGER
)""")
```

### Добавить новую апись
INSERT
INSERT INTO <table_name> (<column_name1>, <column_name2>, ...) VALUES (<value1>, <value2>, …)\
или:\
INSERT INTO <table_name> VALUES (<value1>, <value2>, …)
```
INSERT INTO users (name, old, score) VALUES('Алексей', 18, 1000)
# or
INSERT INTO users VALUES('Михаил', 1, 19, 1000)
```
### Выборка данных из таблици
SELECT
SELECT col1, col2, … FROM <table_name>
```
SELECT name, old, score FROM users
# or
SELECT * FROM users
```
### Фильтр
WHERE
SELECT col1, col2, … FROM <table_name> WHERE <условие>
```
SELECT * FROM users WHERE score < 1000
```
условие
= или ==, >, <, >=, <=, !=, BETWEEN

- AND – условное И: exp1 AND exp2. Истинно, если одновременно истинны exp1 и exp2.
- OR – условное ИЛИ: exp1 OR exp2. Истинно, если истинно exp1 или exp2 или оба выражения.
- NOT – условное НЕ: NOT exp. Преобразует ложное условие в истинное и, наоборот, истинное – в ложное.
- IN – вхождение во множество значений: col IN (val1, val2, …)
- NOT IN – не вхождение во множество значений: col NOT IN (val1, val2, …)

```
SELECT * FROM users WHERE old IN(19, 32) AND score > 300 OR sex = 1
SELECT * FROM users WHERE (old IN(19, 32) OR sex = 1) AND score > 300
SELECT * FROM users WHERE old IN(19, 32) AND NOT score > 300
```

### Сортировка
ORDER BY
```
SELECT * FROM users WHERE score < 1000 ORDER BY old
# по убыванию
SELECT * FROM users WHERE score < 1000 ORDER BY old DESC
# по возрастанию
SELECT * FROM users WHERE score < 1000 ORDER BY old ASC
```

### Ограничение выборки
LIMIT
LIMIT <max> [OFFSET offset]
or
LIMIT <offset, max>
```
SELECT * FROM users WHERE score > 100 ORDER BY score DESC LIMIT 5
# OFFSET n пропутить первых записей
SELECT * FROM users WHERE score > 100 ORDER BY score DESC LIMIT 5 OFFSET 2
# or
SELECT * FROM users WHERE score > 100 ORDER BY score DESC LIMIT 2, 5
```

### python
```
import sqlite3 as sq

with sq.connect("saper.db") as con:
    cur = con.cursor()

    cur.execute("SELECT * FROM users WHERE score > 100 ORDER BY score DESC LIMIT 5")
    result = cur.fetchall()
    print(result)

    for result in cur:
        print(result)

# fetchmany(size) – возвращает число записей не более size;
# fetchone() – возвращает первую запись.

    result = cur.fetchone()
    result2 = cur.fetchmany(2)
    print(result)
    print(result2)      
```
### Изменение данных в записях
UPDATE
UPDATE имя_таблицы SET имя_столбца = новое_значение WHERE условие
```
# во всех полях
UPDATE users SET score = 0
# в поле по условию
UPDATE users SET score = 1000 WHERE rowid = 1
# or
UPDATE users SET score = score+500 WHERE sex = 2
# or
UPDATE users SET score = 700, old = 45 WHERE old > 40
# or
UPDATE users SET score = 1500 WHERE name LIKE 'Федор'
# LIKE возвращает True, если поле name содержит имя «Федор»
# '%' - любое продолжение строки;  '_' - любой символ;

UPDATE users SET score = score+100 WHERE name LIKE 'М%'
# or
UPDATE users SET score = score+100 WHERE name LIKE 'С_рг%'
```
### удаление записей из таблицы
DELETE
DELETE FROM имя_таблицы WHERE условие

```
DELETE FROM users WHERE rowid IN(2, 5)
```
### Агрегирование
count(название столбца)
```
SELECT count(user_id) FROM games WHERE user_id = 1
# or
# синоним имя столбца
SELECT count() as count FROM games WHERE user_id = 1
```
агрегирующие функции
- count() – подсчет числа записей;
- sum() – подсчет суммы указанного поля по всем записям выборки;
- avr() – вычисление среднего арифметического указанного поля;
- min() – нахождение минимального значения для указанного поля;
- max() – нахождение максимального значения для указанного поля.

```
# уникальные поля
SELECT count(DISTINCT user_id) as count FROM games

SELECT DISTINCT user_id FROM games

SELECT sum(score) as sum FROM games WHERE user_id = 1

SELECT max(score) FROM games WHERE user_id = 1

SELECT min(score) FROM games WHERE user_id = 1
```
### Группировка
GROUP BY
GROUP BY <имя поля>

```
SELECT user_id, sum(score) as sum
FROM games
GROUP BY user_id

# поля по условию сортировка по сумме с убыванием
# с ограничением числа записей
SELECT user_id, sum(score) as sum
FROM games
WHERE score > 300
GROUP BY user_id
ORDER BY sum DESC
LIMIT 10
```
### Сводные таблицы
JOIN
JOIN <таблица> ON <условие связывания>

SELECT <поля> FROM <таблица 1>
JOIN <таблица 2> JOIN <таблица 3> … JOIN <таблица N>
ON <условие связывания>
```
# сводные данные с полями name, sex, score
# условие связывания ON games.user_id = users.rowid
SELECT name, sex, games.score FROM games
JOIN users ON games.user_id = users.rowid
# or
SELECT name, sex, games.score FROM games
INNER JOIN  users ON games.user_id = users.rowid

SELECT name, sex, games.score FROM users, games
# все записи из главной таблицы (games), а дополнительные сведения из второй таблицы добавлять, если они там есть
SELECT name, sex, games.score FROM games
LEFT JOIN users ON games.user_id = users.rowid

SELECT name, sex, sum(games.score) as score
FROM games
JOIN users ON games.user_id = users.rowid
GROUP BY user_id
ORDER BY score DESC
```

### Объединения нескольких таблиц
UNION
(слияние)

```
SELECT score, `from` FROM tab1
UNION SELECT val, type FROM tab2
# `from` как поле, а не оператор FROM
# выведит количество запиесей score+val и `from`+type
```
Повторяющиеся значения полей не выводятся, только уникальные записи
```
SELECT score FROM tab1
UNION SELECT val FROM tab2
```

```
# фильтр и ограничение максимального числа записей
SELECT score, 'table 1' as tbl FROM tab1 WHERE score IN(300, 400)
UNION SELECT val, 'table 2' FROM tab2
ORDER BY score DESC
LIMIT 3
```
### Вложенные SQL-запросы

два запроса
```
SELECT mark FROM marks
WHERE id = 2 AND subject LIKE 'Си'

SELECT name, subject, mark FROM marks
JOIN students ON students.rowid = marks.id
WHERE mark > 3 AND subject LIKE 'Си'
```
один запрос
```
SELECT name, subject, mark FROM marks
JOIN students ON students.rowid = marks.id
WHERE mark > (SELECT mark FROM marks
WHERE id = 2 AND subject LIKE 'Си')
AND subject LIKE 'Си'
```
если воженный запрос возвращает несколько значений \
то берется первое значение остальные отбрасываются
```
SELECT name, subject, mark FROM marks
JOIN students ON students.rowid = marks.id
WHERE mark > (SELECT mark FROM marks WHERE id = 2 )
AND subject LIKE 'Си'
```
с агрегирующей функцией
```
SELECT name, subject, mark FROM marks
JOIN students ON students.rowid = marks.id
WHERE mark > (SELECT avg(mark) FROM marks WHERE id = 2 )
AND subject LIKE 'Си'
```
### Вложения в команде INSERT
```
INSERT INTO female (SELECT * FROM students WHERE sex = 2)
# or
INSERT INTO female
SELECT * FROM students WHERE sex = 2

# исключаем первое поля на NULL
# вместо него сгенерирует уникальный ключ для добавляемых записей
INSERT INTO female
SELECT NULL, name, sex, old FROM students WHERE sex = 2
```
### Вложения в команде UPDATE
```
UPDATE marks SET mark = 0
WHERE mark <= (SELECT min(mark) FROM marks WHERE id = 1)
```
### Вложения в команде DELETE
```
DELETE FROM students
WHERE old < (SELECT old FROM students WHERE id = 2)
```
### Методы execute, executemany, executescript, commit, rollback
```
import sqlite3 as sq

with sq.connect("cars.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS cars (
        car_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    )""")

    # con.commit() – применение всех изменений в таблицах БД;
    # con.close() – закрытие соединения с БД.
```
Методы execute, executemany и executescript
```
cur.execute("INSERT INTO cars VALUES(1,'Audi',52642)")
cur.execute("INSERT INTO cars VALUES(2,'Mercedes',57127)")
cur.execute("INSERT INTO cars VALUES(3,'Skoda',9000)")
cur.execute("INSERT INTO cars VALUES(4,'Volvo',29000)")
cur.execute("INSERT INTO cars VALUES(5,'Bentley',350000)")

# or

cars = [
    ('Audi', 52642),
    ('Mercedes', 57127),
    ('Skoda', 9000),
    ('Volvo', 29000),
    ('Bentley', 350000)
]
# cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", cars[0])
for car in cars:
    cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)

#or

cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)

# именованные параметры (плейсхолдеры) (price = 0)
cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'A%'", {'Price': 0})
```
несколько отдельных SQL-команд executescript
```
cur.executescript("""DELETE FROM cars WHERE model LIKE 'A%';
    UPDATE cars SET price = price+1000
""")
```
### Методы commit и rollback
```
con = None
try:
    con = sq.connect("cars.db")
    cur = con.cursor()

    cur.executescript("""CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price INTEGER
        );
        BEGIN;
        INSERT INTO cars VALUES(NULL,'Audi',52642);
        INSERT INTO cars VALUES(NULL,'Mercedes',57127);
        INSERT INTO cars VALUES(NULL,'Skoda',9000);
        INSERT INTO cars VALUES(NULL,'Volvo',29000);
        INSERT INTO cars VALUES(NULL,'Bentley',350000);
        UPDATE cars SET price = price+1000
    """)
    con.commit()

except sq.Error as e:
    if con: con.rollback() # откатить до исходного состояния
    print("Ошибка выполнения запроса")
finally:
    if con: con.close()
```

```
with sq.connect("cars.db", isolation_level=None) as con:
    cur = con.cursor()

    cur.executescript("""INSERT INTO cars VALUES(NULL,'Audi',52642);
        INSERT INTO cars VALUES(NULL,'Mercedes',57127);
        INSERT INTO cars VALUES(NULL,'Skoda',9000);
        INSERT INTO cars VALUES(NULL,'Volvo',29000);
        INSERT INTO cars VALUES(NULL,'Bentley',350000);
    """)
```

### Свойство lastrowid
```
with sq.connect("cars.db") as con:
    cur = con.cursor()

    cur.executescript("""CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price INTEGER
        );
        CREATE TABLE IF NOT EXISTS cust(name TEXT, tr_in INTEGER, buy INTEGER);        
    """)

    cur.execute("INSERT INTO cars VALUES(NULL,'Запорожец', 1000)")

    last_row_id = cur.lastrowid  # значение rowid последней добавленной записи
    buy_car_id = 2
    cur.execute("INSERT INTO cust VALUES('Федор', ?, ?)", (last_row_id, buy_car_id))
```
### методы fetchall, fetchmany, fetchone, iterdump
- fetchall() – возвращает число записей в виде упорядоченного списка;
- fetchmany(size) – возвращает число записей не более size;
- fetchone() – возвращает первую запись.
```
import sqlite3 as sq

cars = [
    ('Audi', 52642),
    ('Mercedes', 57127),
    ('Skoda', 9000),
    ('Volvo', 29000),
    ('Bentley', 350000)
]

with sq.connect("cars.db") as con:
    con.row_factory = sq.Row  # реультат выорки как словари
    #  
    # <sqlite3.Row object at 0x00000185B226B8B0>
    cur = con.cursor()

    cur.executescript("""CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price INTEGER)
    """)

    cur.executemany("INSERT INTO cars VALUES(NULL,?, ?)", cars)

    cur.execute("SELECT model, price FROM cars")
    rows = cur.fetchall()  # записи
    print(rows)
    # [('Audi', 52642), ('Mercedes', 57127), ('Skoda', 9000), ('Volvo', 29000), ('Bentley', 350000)]
    rows = cur.fetchone()  # первая запись
    rows = cur.fetchmany(4) # n записей
    # [('Audi', 52642), ('Mercedes', 57127), ('Skoda', 9000), ('Volvo', 29000)]

    # использование как итерируемый объект
    for result in cur:
      # print(result)  # бес con.row_factory = sq.Row
      print(result['model'], result['price']) # при con.row_factory = sq.Row


```
### Хранение изображений в БД
```
cur.executescript("""CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    ava BLOB,
    score INTEGER)
""")

def readAva(n):
    try:
        with open(f"avas/{n}.png", "rb") as f:
            return f.read()
    except IOError as e:
        print(e)
        return False

img = readAva(1)
if img:
    binary = sq.Binary(img)
    cur.execute("INSERT INTO users VALUES ('Николай', ?, 1000)", (binary,))


```
рочитаем изображение из этого поля
```
cur.execute("SELECT ava FROM users LIMIT 1")
img = cur.fetchone()['ava']

def writeAva(name, data):
    try:
        with open(name, "wb") as f:
            f.write(data)
    except IOError as e:
        print(e)
        return False

    return True

writeAva("out.png", img)

```
### Создание бэкапа БД
iterdump()
```
with sq.connect("cars.db") as con:
    cur = con.cursor()

    for sql in con.iterdump():
        print(sql)

# ->
BEGIN TRANSACTION;
CREATE TABLE cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            model TEXT,
            price INTEGER);
INSERT INTO "cars" VALUES(1,'Audi',0);
INSERT INTO "cars" VALUES(2,'Mercedes',57127);
INSERT INTO "cars" VALUES(3,'Skoda',9000);
INSERT INTO "cars" VALUES(4,'Volvo',29000);
INSERT INTO "cars" VALUES(5,'Bentley',350000);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('cars',5);
CREATE TABLE users (
            name TEXT,
            ava BLOB,
            score INTEGER);
INSERT INTO "users" VALUES('Николай', …,1000);
COMMIT;

# сохранить в отдельный файл
with open("sql_damp.sql", "w") as f:
        for sql in con.iterdump():
            f.write(sql)

# восстановить БД
with open("sql_damp.sql", "r") as f:
        sql = f.read()
        cur.executescript(sql)

```
### Создание БД в памяти
```
data = [("car", "машина"), ("house", "дом"), ("tree", "дерево"), ("color", "цвет")]

con = sq.connect(':memory:')
with con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS dict(
        eng TEXT, rus TEXT    
    )""")

    cur.executemany("INSERT INTO dict VALUES(?,?)", data)

    cur.execute("SELECT rus FROM dict WHERE eng LIKE 'c%'")
    print(cur.fetchall())
```
### keywords SQLite
 sqlite3_keyword_count(), sqlite3_keyword_name(), and sqlite3_keyword_check()

| keywords | keywords | keywords |
| ----- | ------ | --- |
| ABORT | ACTION | ALL |
| ADD   | AFTER  | ALTER |
| ALTER | ALWAYS |  ANALYZE |
| AND | AS |  ASC | ATTACH |
| AUTOINCREMENT | BEFORE | BEGIN |
| BETWEEN | BY | CASCADE |
| CASE | CAST | CHECK |
| COLLATE | COLUMN | COMMIT |
| CONFLICT | CONSTRAINT | CREATE |
| CROSS | CURRENT | CURRENT_DATE |
| CURRENT_TIME | CURRENT_TIMESTAMP | DATABASE |
| DEFAULT | DEFERRABLE | DEFERRED |
| DELETE | DESC | DETACH |
| DISTINCT | DO | DROP |
| EACH | ELSE | END |
| ESCAPE | EXCEPT | EXCLUDE |
| EXCLUSIVE | EXISTS | EXPLAIN |
| FAIL | FILTER | FIRST |
| FOLLOWING | FOR | FOREIGN |
| FROM | FULL | GENERATED |
| GLOB | GROUP | GROUPS |
| HAVING | IF | IGNORE |
| IMMEDIATE | IN | INDEX |
| INDEXED | INITIALLY | INNER |
| INSERT | INSTEAD | INTERSECT |
| INTO | IS | ISNULL |
| JOIN | KEY | LAST |
| LEFT | LIKE | LIMIT |
| MATCH | NATURAL | NO |
| NOT | NOTHING | NOTNULL |
| NULL | NULLS | OF |
| OFFSET | ON | OR |
| ORDER | OTHERS | OUTER |
| OVER | PARTITION | PLAN |
| PRAGMA | PRECEDING | PRIMARY |
| QUERY | RAISE | RANGE |
| RECURSIVE | REFERENCES | REGEXP |
| REINDEX | RELEASE | RENAME |
| REPLACE | RESTRICT | RIGHT |
| ROLLBACK | ROW | ROWS |
| SAVEPOINT | SELECT | SET |
| TABLE | TEMP | TEMPORARY |
| THEN | TIES | TO |
| TRANSACTION | TRIGGER | UNBOUNDED |
| UNION | UNIQUE | UPDATE |
| USING | VACUUM | VALUES |
| VIEW | VIRTUAL | WHEN |
| WHERE | WINDOW | WITH |
| WITHOUT | | |

---
## sqlite help

[SQLite tutorials](http://sqlitetutorials.com/sqlite-intro.html#contact)

relational database ->
	Database -> collection tables
	Table -> organized Record (or row) Field (or column)
	Record
	Field


SELECT * FROM TableNamme; # Fetch all the data form the table
```
keywords:
aggregate functions
ALTER TABLE
ANALYZE
ATTACH DATABASE
BEGIN TRANSACTION
comment
COMMIT TRANSACTION
core functions
CREATE INDEX
CREATE TABLE
CREATE TRIGGER
CREATE VIEW
CREATE VIRTUAL TABLE
date and time functions
DELETE
DETACH DATABASE
DROP INDEX
DROP TABLE
DROP TRIGGER
DROP VIEW
END TRANSACTION
EXPLAIN
expression
INDEXED BY
INSERT
keywords
ON CONFLICT clause
PRAGMA
REINDEX
RELEASE SAVEPOINT
REPLACE
ROLLBACK TRANSACTION
SAVEPOINT
SELECT
UPDATE
VACUUM
WITH clause
```
## Functions
```
  SqLite - Functions
  SqLite - Avg()
  SqLite - Count()
  SqLite - First()
  SqLite - Last()
  SqLite - Max()
  SqLite - Min()
  SqLite - Sum()
  SqLite - Group By
  SqLite - Having
  SqLite - Ucase()
  SqLite - Lcase()
  SqLite - Mid()
  SqLite - Len()
  SqLite - Round()
  SqLite - Now()
  SqLite - Format()
```
## Content
```
  SqLite - Syntax
  SqLite - Data Types
  SqLite - Create DB
  SqLite - Create Table
  SqLite - Select
  SqLite - Distinct
  SqLite - Where
  SqLite - And & Or
  SqLite - Order By
  SqLite - Insert Into
  SqLite - Update
  SqLite - Delete
  SqLite - Injection
  SqLite - Select Top
  SqLite - Like
  SqLite - Wildcards
  SqLite - In
  SqLite - Between
  SqLite - Aliases
  SqLite - Joins
  SqLite - Inner Join
  SqLite - Left Join
  SqLite - Right Join
  SqLite - Full Join
  SqLite - Union
  SqLite - Select Into
  SqLite - Insert Into Select
  SqLite - Constraints
  SqLite - Not Null
  SqLite - Unique
  SqLite - Primary Key
  SqLite - Foreign Key
  SqLite - Check
  SqLite - Default
  SqLite - Create Index
  SqLite - Drop
  SqLite - Alter
  SqLite - Auto Increment
  SqLite - Views
  SqLite - Dates
  SqLite - Null Values
  SqLite - Null Functions
  SqLite - Data Types
  SqLite - DB Data Types
```
