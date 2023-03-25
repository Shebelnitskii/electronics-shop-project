from src.item import Item

class KeyBoard(Item):
    def __init__(self,name: str, price: float, quantity: int):
        super().__init__(name,price,quantity)
        self.__language = "EN"


    def change_lang(self):
        if self.__language == "RU":
            self.__language = "EN"
        else:
            self.__language = "RU"
        return self


    @property
    def language(self):
        return self.__language
    @language.setter
    def language(self, language):
        if language != "EN" or language != "RU":
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")
