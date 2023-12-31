import requests


class HH():
    def __init__(self, id):
        self.__count = 500
        self.id = id


    #Получаем вакансии из HH.ru

    def get_request(self):
        pages = int(self.__count / 100)
        params = {
            "page": 0,
            "per_page": 100,
            "employer_id": self.id
        }
        response = []

        for page in range(pages+1):
            params.update({"page": page})
            data = requests.get(f"https://api.hh.ru/vacancies", params=params)
            try:
                items = data.json()
                response += items['items']
            except KeyError:
                print("Ключ 'items' отсутствует в JSON-ответе")
        return response

    # def items(self):
    #     for i in self.get_request():
    #         return i['items']


    def items_1(self):
        descr = []
        salary = []
        link = []
        count = -1
        new_dict = []
        emp_name = ''

        for i in self.get_request():
            if self.id == 4519033:
                emp_name = 'Вэбиум'
            elif self.id == 2014445:
                emp_name = 'ИМК'
            elif self.id == 2968758:
                emp_name = 'Смарт Конекшн'
            elif self.id == 2492666:
                emp_name = 'Color-Express'
            elif self.id == 72977:
                emp_name = 'Барса'
            elif self.id == 3742187:
                emp_name = 'ПроТекс'
            elif self.id == 1684162:
                emp_name = '7 этажей'
            elif self.id == 4297447:
                emp_name = 'Джойсити'
            elif self.id == 2905714:
                emp_name = 'Чик-Чирик'
            elif self.id == 5250113:
                emp_name = 'Джи Си Рест'

            descr.append(i['name'])
            salary.append(i['salary'])
            link.append(i['url'])
            count += 1
            employer_info = {'employer_name': emp_name, 'employer_descr': descr[count], 'employer_salary': salary[count],
                     'employer_link': link[count]}
            new_dict.append(employer_info)

        return new_dict


    # Метод основную инфмормаци добавляет в словарь, а также работает с зарплатой, а именно выводит зарплату среднуюю зарплату
    # если есть вилка от и до, а также переводит в рубли зарпалут из Казахстана и Беларусии
    def information(self):
        salary = []
        count = -1
        new_dict = []
        for sal in self.items_1():
            if sal['employer_salary'] is None:
                salary.append(0)
            elif sal['employer_salary']['currency'] == 'KZT':
                from_salary = sal['employer_salary']['from'] if isinstance(sal['employer_salary']['from'], int) else 0
                to_salary = sal['employer_salary']['to'] if isinstance(sal['employer_salary']['to'], int) else 0
                if to_salary != None:
                    salary.append(((from_salary + to_salary) / 2) / 5)
                else:
                    salary.append(from_salary / 5)
            elif sal['employer_salary']['currency'] == 'BYR':
                from_salary = sal['employer_salary']['from'] if isinstance(sal['employer_salary']['from'], int) else 0
                to_salary = sal['employer_salary']['to'] if isinstance(sal['employer_salary']['to'], int) else 0
                if to_salary != None:
                    salary.append(((from_salary + to_salary) / 2) * 28)
                else:
                    salary.append(from_salary * 28)
            else:
                from_salary = sal['employer_salary']['from'] if isinstance(sal['employer_salary']['from'], int) else 0
                to_salary = sal['employer_salary']['to'] if isinstance(sal['employer_salary']['to'], int) else 0
                if to_salary != None:
                    salary.append((from_salary + to_salary) / 2)
                else:
                    salary.append(from_salary)

        for i in self.items_1():
            count += 1
            new_dict.append({'employer_name': i['employer_name'], 'employer_descr': i['employer_descr'],
                             'employer_salary': salary[count], 'employer_link': i['employer_link']})

        return new_dict






