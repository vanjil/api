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
