from src.item import Item

class Mixin(Item):
    def __init__(self,name: str, price: float, quantity: int):
        super().__init__(name,price,quantity)
        self._language = 'EN'

    @property
    def language(self):
        return self._language
    @language.setter
    def language(self, language):
        if language != "EN" or language != "RU":
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'
        return self

class KeyBoard(Mixin):
    def __init__(self,name: str, price: float, quantity: int):
        super().__init__(name,price,quantity)