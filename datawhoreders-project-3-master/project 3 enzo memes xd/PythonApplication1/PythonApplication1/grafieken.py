from database import Database as d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['toolbar'] = 'None'

class create_crime_graph:
    def __init__(self, jaar, soort):
        N = 10
        crime = []
        police = []
        for wijk in d.get_areas("criminaliteit"):
            a = wijk[0]
            result = d.get_crime_data(soort, jaar, ("'" + a + "'"))
            crime.append(result)
            bureaus = d.get_police_data(("'" + a + "'"))
            police.append(bureaus)
        tuple_result = tuple(crime)
        tuple_police = tuple(police)
        ind = np.arange(N)
        width = 0.35
        fig, ax = plt.subplots()
        rects1 = ax.bar(ind, tuple_result, width, color = "r")
        rects2 = ax.bar(ind + width, tuple_police, width, color = "b")
        ax.set_ylabel("% criminaliteit/het aantal politiebureaus")
        ax.set_title("Percentage " + str(soort) + " criminaliteit + aantal politiebureaus " + str(jaar))
        ax.set_xticks(ind + width / 2)
        volgorde = []
        for wijk in d.get_areas("criminaliteit"):
            volgorde.append(wijk[0])
        ax.set_xticklabels(tuple(volgorde))
        ax.legend((rects1[0], rects2[0]), ("Percentage criminaliteit", "Aantal politiebureaus"))

        def autolabel(rects):
            for rect in rects:
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width()/2., height, '%d' % int(height), ha='center', va='bottom')

        autolabel(rects1)
        autolabel(rects2)
        plt.show()
