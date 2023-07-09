import psycopg2

class DBManager():

    def get_companies_and_vacancies_count(self):
        conn = psycopg2.connect(database="vacansy",
                                user="pavel",
                                password="password",
                                host="localhost")
        cur = conn.cursor()

        cur.execute("SELECT employer_name, COUNT(*) FROM job GROUP BY employer_name")
        rows = cur.fetchall()

        return rows

    def get_all_vacancies(self):
        conn = psycopg2.connect(database="vacansy",
                                user="pavel",
                                password="password",
                                host="localhost")
        cur = conn.cursor()
        cur.execute("SELECT employer_name, employer_information, employer_salary, employer_link FROM job")
        rows = cur.fetchall()

        return rows

    def get_avg_salary(self):
        conn = psycopg2.connect(database="vacansy",
                                user="pavel",
                                password="password",
                                host="localhost")
        cur = conn.cursor()
        cur.execute("SELECT ROUND(AVG(employer_salary), 2) FROM employers")
        average_salary = cur.fetchone()[0]
        return average_salary

    def get_vacancies_with_higher_salary(self):
        conn = psycopg2.connect(database="vacansy",
                                user="pavel",
                                password="password",
                                host="localhost")
        cur = conn.cursor()

        cur.execute("SELECT * FROM job WHERE employer_salary > (SELECT ROUND(AVG(employer_salary), 2) FROM job)")
        higher_salary_vacancies = cur.fetchall()
        return higher_salary_vacancies

    def get_vacancies_with_keyword(self, keyword):
        conn = psycopg2.connect(database="vacansy",
                                user="pavel",
                                password="password",
                                host="localhost")
        cur = conn.cursor()

        cur.execute("SELECT employer_name, employer_information, employer_salary, employer_link FROM job WHERE LOWER(employer_information) LIKE %s", ('%' + keyword + '%',))
        vacancies = cur.fetchall()
        return vacancies

a = DBManager()
print(a.get_vacancies_with_higher_salary())