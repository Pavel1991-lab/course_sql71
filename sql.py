import psycopg2

from __init__ import HH



# Подключение к базе данных
conn = psycopg2.connect(database="vacansy",
                        user="pavel",
                        password="password",
                        host="localhost")
cur = conn.cursor()

employer_addresses = HH()

for employer_info in employer_addresses.information():
    employer_name = employer_info['employer_name']
    employer_information = employer_info['employer_descr']
    employer_salary =  employer_info['employer_salary']
    employer_link  =  employer_info['employer_link']

    # Формирование SQL-запроса для вставки данных
    sql = "INSERT INTO job (id, employer_name, employer_information, employer_salary, employer_link) VALUES (DEFAULT, %s, %s, %s, %s)"

    # Выполнение SQL-запроса с передачей данных
    cur.execute(sql, (employer_name, employer_information, employer_salary, employer_link))

# Фиксация изменений и закрытие соединения
conn.commit()
cur.close()
conn.close()