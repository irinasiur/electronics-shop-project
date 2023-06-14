from src.item import Item


class MixinLog:
    LANGUAGE = "EN"

    def __init__(self):
        self.__language = self.LANGUAGE

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, a):
        if a != "EN":
            if a != "RU":
                print("AttributeError: property 'language' of 'KeyBoard' object has no setter")

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
            return self
        if self.__language == "RU":
            self.__language = "EN"
            return self


class Keyboard(Item, MixinLog):
    pass
