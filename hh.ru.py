import requests


class HH():
    def __init__(self):
        self.__count = 500


    #Получаем вакансии из HH.ru

    def get_request(self, id):
        pages = int(self.__count / 100)
        params = {
            "page": 0,
            "per_page": 100,
            "employer_id": id
        }
        response = []
        for page in range(pages):
            params.update({"page": page})
            data = requests.get(f"https://api.hh.ru/vacancies", params=params)
            try:
                items = data.json()
                # for item in items:
                #     if item['employer']['name'] in ['Яндекс', 'Camilla Coffee', 'АРТИТЕРА', 'Детективное Агентство Главк', 'Альбатрос', 'КлеверИнвест', 'Sip Direction', 'Барса', 'Фемави', 'Смарт Конекшн']:
                response.append(items)
            except KeyError:
                print("Ключ 'items' отсутствует в JSON-ответе")
        return response


    #Получаем основную информацию которую будем использовать в базе данных
    def get__name_employer(self,id):
        employer_addresses = []
        empl = ''
        for vacancy in self.get_request(id):
            employer = vacancy['items']
            for i in employer:
                employer_name = i['name']
                employer_salary = i['salary']
                employer_link = i['url']
            if id == 1740:
                empl = 'яндекс'
            elif id == 2180:
                empl = 'озон'
            employer_info = {'empoloyer': empl, 'employer_descr': employer_name, 'employer_salary': employer_salary, 'employer_link': employer_link}
            employer_addresses.append(employer_info)

        return employer_addresses


    #Метод основную инфмормаци добавляет в словарь, а также работает с зарплатой, а именно выводит зарплату среднуюю зарплату
    #если есть вилка от и до, а также переводит в рубли зарпалут из Казахстана и Беларусии
    def information(self, id):
        salary = []
        count = -1
        new_dict = []
        for sal in self.get_name_employer(id):

            if sal['employer_salary']['currency'] == 'KZT':
                if sal['employer_salary']['to'] != None:
                    salary.append(((sal['employer_salary']['from']+ sal['employer_salary']['to'])/2) / 5)
                else:
                    salary.append(sal['employer_salary']['from'] / 5)
            elif sal['employer_salary']['currency'] == 'BYR':
                if sal['employer_salary']['to'] != None:
                    salary.append(((sal['employer_salary']['from']+ sal['employer_salary']['to'])/2) * 28)
                else:
                    salary.append(sal['employer_salary']['from'] * 28)
            else:
                if sal['employer_salary']['to'] != None:
                    salary.append((sal['employer_salary']['from']+ sal['employer_salary']['to'])/2)
                else:
                    salary.append(sal['employer_salary']['from'])

        for i in self.get_name_employer():
            count += 1
            new_dict.append({'employer_name': i['employer_name'], 'employer_desc': i['employer_desc'], 'employer_salary': salary[count], 'employer_link': i['employer_link']})

        return new_dict


a = HH()


print(a.get_request(1740))


