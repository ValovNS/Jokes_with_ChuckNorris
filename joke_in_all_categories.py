import requests
class CreateJoke():

    """Класс включающий сценарии по отправке запросов, с целью получения категорий шуток с Чаком Норрисом,а также выводит все 16 категорий шуток"""

    url = "https://api.chucknorris.io/jokes/categories"

    def check_status_code(self,result,check_type):  # Функция, которая получает результат запроса и тип проверки, проверяет статус-код
        print(f"Статус-код запроса на {check_type}: {result.status_code}""")
        assert result.status_code == 200, "ОШИБКА, Статус-код некорректен"

    def get_categories(self):  # Функция, которая возвращает категории
        print(self.url)
        result = requests.get(self.url)
        self.check_status_code(result,"получение категорий")
        return result.json()

    def get_joke(self, category:str):  # Функция, которая возвращает шутку по категории
        joke_url = f"https://api.chucknorris.io/jokes/random?category={category}"
        result = requests.get(joke_url)
        joke = result.json()["value"]
        self.check_status_code(result,"получение шутки")
        return joke

    def joke_in_category(self):  # Функция, которая выводит список категорий и соответствующие шутки
        categories = self.get_categories()
        print(f"Список категорий:{categories}")
        for category in categories:
            joke=self.get_joke(category)
            print(f"Категория: {category} - Шутка: {joke}")


start = CreateJoke()
start.joke_in_category()