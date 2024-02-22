class Vacancy:
    def __init__(self, title: str, link: str, salary: str, description: str):
        self.title = title
        self.link = link
        self.salary = salary
        self.description = description

    def __repr__(self) -> str:
        return f"Vacancy(title={self.title}, salary={self.salary})"

    def __eq__(self, other: 'Vacancy') -> bool:
        return self.salary == other.salary

    def __lt__(self, other: 'Vacancy') -> bool:
        return self.salary < other.salary
