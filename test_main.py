import pytest
from main import HeadHunterAPI


@pytest.fixture
def mock_hh_api():
    class MockHeadHunterAPI(HeadHunterAPI):
        def get_vacancies(self, search_query):
            # Возвращаем заранее заданные вакансии для тестов
            return [
                {"name": "Python Developer", "url": "https://example.com", "salary": "100 000 руб.", "description": "Python developer job description"},
                {"name": "Java Developer", "url": "https://example.com", "salary": "80 000 руб.", "description": "Java developer job description"},
                {"name": "Frontend Developer", "url": "https://example.com", "salary": "120 000 руб.", "description": "Frontend developer job description"}
            ]

    return MockHeadHunterAPI()

def test_get_vacancies_successful(mock_hh_api):
    # Проверка успешного запроса вакансий из API
    hh_vacancies = mock_hh_api.get_vacancies("Python")
    assert len(hh_vacancies) == 3
    assert all(isinstance(vacancy, dict) for vacancy in hh_vacancies)


def test_get_vacancies_empty(mock_hh_api, monkeypatch):
    # Мокаем запрос, чтобы возвращалась пустая список вакансий
    monkeypatch.setattr(mock_hh_api, 'get_vacancies', lambda _: [])

    hh_vacancies = mock_hh_api.get_vacancies("Python")
    assert hh_vacancies == []
