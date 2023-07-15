# В этом модуле мы создаем таблицу и подключаемся к базе данных

from DBManager import DBManager



company_and_id = {
    'Вэбиум': 4519033,
    'ИМК': 2014445,
    'Смарт Конекшн': 2968758,
    'Color-Express': 2492666,
    'Барса': 72977,
    'ПроТекс': 3742187,
    '7 этажей': 1684162,
    'Джойсити': 4297447,
    'Чик-Чирик': 2905714,
    'Джи Си Рест': 5250113
}

for company, id in company_and_id.items():
    db_manager = DBManager(id)
    db_manager.create_database()
