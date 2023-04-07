# друге завдання
class TextProcessor:
    def __init__(self):
        # список знаків пунктуації (які потім удалимо)
        self._puncts = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    def get_clean_string(self, text):
        # метод, який убирає знаки пунктуації
        clean_text = ""
        for c in text:
            if not self.is_punct(c):
                clean_text += c
        return clean_text

    def is_punct(self, c):
        # перевірка дійсно знак пунктуації
        return c in self._puncts

class TextLoader:
    def __init__(self):
        # створюємо об'єкт
        self._text_processor = TextProcessor()
        # рядок з очищеним текстом
        self._clean_string = ""

    def set_clean_text(self, text):
        # викликаємо метод, щоб очистити текст
        self._clean_string = self._text_processor.get_clean_string(text)

    @property
    def clean_string(self):
        # повертає очищений текст та виводить повідомлення
        print("Очищений текст:")
        return self._clean_string

class DataInterface:
    def __init__(self):
        # створюємо об'єкт класу TextLoader
        self._text_loader = TextLoader()

    def process_texts(self, texts):
        # цикл, який обробляє кожен текст зі списку
        for text in texts:
            self._text_loader.set_clean_text(text)
            print(self._text_loader.clean_string)

# Приклад використання класу DataInterface
data_interface = DataInterface()
data_interface.process_texts(["Це! тестовий текст, що. потрібно -очистити. тут бага&то всяких %розділови?х/ знаків!"])
