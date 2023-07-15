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

Vebium = DBManager(company_and_id['Вэбиум'])
IMK = DBManager(company_and_id['ИМК'])
Smart_Connection = DBManager(company_and_id['Смарт Конекшн'])
Color_Express = DBManager(company_and_id['Color-Express'])
Barsa = DBManager(company_and_id['Барса'])
ProTex = DBManager(company_and_id['ПроТекс'])
Seven_Floors = DBManager(company_and_id['7 этажей'])
JoyCity = DBManager(company_and_id['Джойсити'])
Chik_Chirik = DBManager(company_and_id['Чик-Чирик'])
GC_Rest = DBManager(company_and_id['Джи Си Рест'])


Vebium.create_database()
IMK.create_database()
Smart_Connection.create_database()
Color_Express.create_database()
Barsa.create_database()
ProTex.create_database()
Seven_Floors.create_database()
JoyCity.create_database()
Chik_Chirik.create_database()
GC_Rest.create_database()

