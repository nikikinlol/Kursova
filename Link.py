from urllib.parse import quote
class Link:
    def __init__(self):
        pass

    def enter_the_inf(self):
        print("Потрібно ввести назву міста спочатку на російській потім на англійській, нажміть на enter ще раз після першого вводу")
        x = str(input(("Введіть назву міста:")))
        return x
    def search_per_sinoptik(self, nameLocation):
        geourl = "https://ua.sinoptik.ua/{0}".format(quote(nameLocation))
        return geourl
    def search_per_meteoprog(self, nameLocation):
        geourl  = "https://www.meteoprog.ua/ru/{0}".format(quote(nameLocation))
        return geourl
