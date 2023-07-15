import psycopg2
from __init__ import HH
class DBManager():
    def __init__(self, id):
        self.id = id
        self.conn = psycopg2.connect(database="vacansy",
                                     user="pavel",
                                     password="password",
                                     host="localhost")
        self.cur = self.conn.cursor()

    def create_database(self):
        # Подключение к базе данных
        conn = psycopg2.connect(database="vacansy",
                                user="pavel",
                                password="password",
                                host="localhost")
        cur = conn.cursor()

        # Создание таблицы "job"
        cur.execute('''CREATE TABLE IF NOT EXISTS job (
                        id SERIAL PRIMARY KEY ,
                        employer_name VARCHAR(255) ,
                        employer_information VARCHAR(255),
                        employer_salary integer,
                        employer_link VARCHAR(255)
                    )''')

        employer_addresses = HH(self.id)

        for employer_info in employer_addresses.information():
            employer_name = employer_info['employer_name']
            employer_information = employer_info['employer_descr']
            employer_salary = employer_info['employer_salary']
            employer_link = employer_info['employer_link']

            # Проверка наличия записи в таблице
            cur.execute(
                "SELECT * FROM job WHERE employer_name = %s AND employer_information = %s AND employer_salary = %s AND employer_link = %s",
                (employer_name, employer_information, employer_salary, employer_link))
            existing_row = cur.fetchone()

            if not existing_row:
                # Формирование SQL-запроса для вставки данных
                sql = "INSERT INTO job (id, employer_name, employer_information, employer_salary, employer_link) VALUES (DEFAULT, %s, %s, %s, %s)"

                # Выполнение SQL-запроса с передачей данных
                cur.execute(sql, (employer_name, employer_information, employer_salary, employer_link))

            # Фиксация изменений и закрытие соединения
        conn.commit()
        cur.close()
        conn.close()
    def get_companies_and_vacancies_count(self):
        self.cur.execute("SELECT employer_name, COUNT(*) FROM job GROUP BY employer_name")
        rows = self.cur.fetchall()
        return rows

    def get_all_vacancies(self):
        self.cur.execute("SELECT employer_name, employer_information, employer_salary, employer_link FROM job")
        rows = self.cur.fetchall()
        return rows

    def get_avg_salary(self):
        self.cur.execute("SELECT ROUND(AVG(employer_salary), 2) FROM employers")
        average_salary = self.cur.fetchone()[0]
        return average_salary

    def get_vacancies_with_higher_salary(self):
        self.cur.execute("SELECT * FROM job WHERE employer_salary > (SELECT ROUND(AVG(employer_salary), 2) FROM job)")
        higher_salary_vacancies = self.cur.fetchall()
        return higher_salary_vacancies

    def get_vacancies_with_keyword(self, keyword):
        self.cur.execute("SELECT employer_name, employer_information, employer_salary, employer_link FROM job WHERE LOWER(employer_information) LIKE %s", ('%' + keyword + '%',))
        vacancies = self.cur.fetchall()
        return vacancies


