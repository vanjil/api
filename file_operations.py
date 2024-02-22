from abc import ABC, abstractmethod
import json

class AbstractVacancySaver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

class JSONSaver(AbstractVacancySaver):
    def __init__(self, filename: str):
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
