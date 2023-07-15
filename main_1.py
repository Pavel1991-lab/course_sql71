#  Здесь работаем с методами класса DBManager

from create_database import  db_manager

print(db_manager.get_all_vacancies())
print()
print(db_manager.get_companies_and_vacancies_count())
print()
print(db_manager.get_avg_salary())
print()
print(db_manager.get_vacancies_with_higher_salary())
print()
print(db_manager.get_vacancies_with_keyword('продавец-консультант'))
