from api import HeadHunterAPI
from models import Vacancy
from file_operations import JSONSaver
from utils import user_interaction

if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies("Python")

    vacancies_list = []
    for item in hh_vacancies:
        title = item.get('name', '')
        link = item.get('url', '')
        salary = item.get('salary', '')
        description = item.get('description', '')
        vacancy = Vacancy(title, link, salary, description)
        vacancies_list.append(vacancy)

    json_saver = JSONSaver("vacancies.json")
    for vacancy in vacancies_list:
        json_saver.add_vacancy(vacancy)

    user_interaction(vacancies_list)
