from Link import Link
from WeatherFather import WeatherFather
class ContentSinoptik(WeatherFather):
    def __init__(self, html, mainClass, mainNextDay, tabsContentInner, temperature, pClassOne, pClassTwo, pClassThree, min, max):
        super(ContentSinoptik, self).__init__(html, mainClass, mainNextDay, tabsContentInner, temperature, pClassOne, pClassTwo, pClassThree, min, max)

    def outputInf(self, weatherList):
        dicSet = Link().enter_the_inf()
        weatherFather = weatherList[0]
        weatherFather2 = weatherList[1]
        weatherFather3 = weatherList[2]

        for i in weatherFather:
            w1 = i
        for i in weatherFather2:
            w2 = i
        for i in weatherFather3:
            w3 = i

        
        print()
        print("------------------------------------------------------")
        print("\t\t\t\t\t\t\t\t\t\tПогода з сайту Sinoptik " + dicSet)
        print("День:" + w1['title'])
        print("Число: " + w1['date1'], ' ', w1['date2'])
        print("Температура: :" + w1['temp'], " ||  " + w1['temp2'])
        print()

        mw2 = []
        for i in w2:
            mw2.append(w2[i])
        mw3 = []
        for i in w3:
            mw3.append(w3[i])
        print("Прогноз на день")
        for i in mw2:
            print(i, end='     ')
        print()
        for j in mw3:
            print(j, end='       ')
            if j == mw3[4]:
                print(end='  ')
            if j == mw3[5]:
                print(end='   ')