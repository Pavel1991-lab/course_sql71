import requests


class HH():
    def __init__(self):
        self.__count = 500

    #Получаем вакансии из HH.ru

    def get_request(self):
        pages = int(self.__count / 100)
        params = {
            "page": 0,
            "per_page": 100,
            "id": 1382065
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
    def get_adress_name_employer(self):
        employer_addresses = []
        for vacancy in self.get_request():
            employer = vacancy['employer']
            employer_name = employer['name']
            employer_address = vacancy['address']
            employer_desc = vacancy['name']
            employer_salary = vacancy['salary']
            employer_link = vacancy['url']

            if employer_address is not None:
                employer_address = employer_address['raw']
            else:
                employer_address = None
            employer_info = {'employer_name': employer_name, 'employer_address': employer_address, 'employer_desc': employer_desc, 'employer_salary': employer_salary, 'employer_link': employer_link}
            employer_addresses.append(employer_info)

        return employer_addresses


    #Метод основную инфмормаци добавляет в словарь, а также работает с зарплатой, а именно выводит зарплату среднуюю зарплату
    #если есть вилка от и до, а также переводит в рубли зарпалут из Казахстана и Беларусии
    def information(self):
        salary = []
        count = -1
        new_dict = []
        for sal in self.get_adress_name_employer():

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

        for i in self.get_adress_name_employer():
            count += 1
            new_dict.append({'employer_name': i['employer_name'], 'employer_address': i['employer_address'], 'employer_desc': i['employer_desc'], 'employer_salary': salary[count], 'employer_link': i['employer_link']})

        return new_dict


a = HH()


print(a.get_request())


