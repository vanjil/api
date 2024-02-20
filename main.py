from abc import ABC, abstractmethod
import json
import requests


class AbstractVacancyAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_query):
        pass


class HeadHunterAPI(AbstractVacancyAPI):
    def get_vacancies(self, search_query):
        response = requests.get(f"https://api.hh.ru/vacancies?text={search_query}")
        if response.status_code == 200:
            return response.json()['items']
        else:
            return []


class Vacancy:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    def to_dict(self):
        return {
            "title": self.title,
            "link": self.link,
            "salary": self.salary,
            "description": self.description
        }

    def __repr__(self):
        return f"Vacancy(title={self.title}, salary={self.salary})"

    def __eq__(self, other):
        return self.salary == other.salary

    def __lt__(self, other):
        return self.salary < other.salary


class AbstractVacancySaver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JSONSaver(AbstractVacancySaver):
    def __init__(self, filename):
        self.filename = filename
        self.vacancies = []

    def add_vacancy(self, vacancy):
        self.vacancies.append(vars(vacancy))
        self.save_to_file()

    def delete_vacancy(self, vacancy):
        self.vacancies.remove(vars(vacancy))
        self.save_to_file()

    def save_to_file(self):
        with open(self.filename, 'w') as f:
            json.dump(self.vacancies, f)


def filter_vacancies(vacancies, keywords):
    return [vacancy for vacancy in vacancies if any(keyword in vacancy.description for keyword in keywords)]


def get_vacancies_by_salary(vacancies, salary_range):
    min_salary, max_salary = map(int, salary_range.split('-'))
    return [vacancy for vacancy in vacancies if min_salary <= int(vacancy.salary) <= max_salary]


def sort_vacancies(vacancies):
    return sorted(vacancies)


def get_top_vacancies(vacancies, top_n):
    return vacancies[:top_n]


def print_vacancies(vacancies):
    for vacancy in vacancies:
        print(vacancy)


def user_interaction(vacancies_list):
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


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
