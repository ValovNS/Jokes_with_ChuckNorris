import requests


class CreateJoke():
    """Класс включающий сценарии по отправке запросов, с целью получения категорий шуток с Чаком Норрисом,а также выводит все 16 категорий шуток"""

    url = "https://api.chucknorris.io/jokes/categories"

    def check_status_code(self, result, check_type):  # Функция, которая получает результат запроса и тип проверки, проверяет статус-код
        print(f"Статус-код запроса на {check_type}: {result.status_code}")
        assert result.status_code == 200, "ОШИБКА, Статус-код некорректен"

    def get_categories(self):  # Функция, которая возвращает категории
        result = requests.get(self.url)
        self.check_status_code(result, "получение категорий")
        return result.json()

    def get_joke(self, category):  # Функция, которая возвращает шутку по категории
        joke_url = f"https://api.chucknorris.io/jokes/random?category={category}"
        result = requests.get(joke_url)
        joke = result.json()["value"]
        self.check_status_code(result, "получение шутки")
        return joke

    def joke_in_category(self, smile: str):  # Функция, которая выводит список категорий и шутку по запрашиваемой категории, если такая категория есть
        categories = self.get_categories()
        print(f"Список категорий:{categories}")
        if smile in categories:
            print(f"Категория: {smile} - Шутка: {self.get_joke(smile)}")
        else:
            print("Такой категории нет")

    def start(self):
        smile = str(input("Введите категорию на английском языке: "))
        print(f"Вы выбрали категорию {smile}")
        self.joke_in_category(smile)


joke = CreateJoke()
joke.start()