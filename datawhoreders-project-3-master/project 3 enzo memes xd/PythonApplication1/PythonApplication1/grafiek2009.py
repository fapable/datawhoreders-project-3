import database as d
import psycopg2
import numpy as np
import matplotlib.pyplot as plt
connection = psycopg2.connect(host = "localhost", dbname = "", user = "postgres", password = "")


N = 10
criminaliteit2009 = (d.get_crime_data("average", "criminaliteit" ,"2009", "'Charlois'"),d.get_crime_data("average", "criminaliteit" ,"2009", "'Delfshaven'") , d.get_crime_data("average", "criminaliteit" ,"2009", "'Feijenoord'"), d.get_crime_data("average", "criminaliteit" ,"2009", "'Hillegersberg-Schiebroek'"), d.get_crime_data("average", "criminaliteit" ,"2009", "'Ijsselmonde'"), d.get_crime_data("average", "criminaliteit" ,"2009", "'Kralingen-Crooswijk'"), d.get_crime_data("average", "criminaliteit" ,"2009", "'Noord'"), d.get_crime_data("average", "criminaliteit" ,"2009", "'Overschie'"), d.get_crime_data("average", "criminaliteit" ,"2009", "'Prins-Alexander'"), d.get_crime_data("average", "criminaliteit" ,"2009", "'Centrum'"))
criminaliteit2009_std = (1, 1, 1, 0, 1, 1, 1, 1, 1, 1)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, criminaliteit2009, width, color='r', yerr=criminaliteit2009_std)

politiebureaus = (d.get_police_data("politiebureau", "politiebureaus", "'Charlois'"), d.get_police_data("politiebureau", "politiebureaus", "'Delfshaven'"), d.get_police_data("politiebureau", "politiebureaus", "'Feijenoord'"), d.get_police_data("politiebureau", "politiebureaus", "'Hillegersberg-Schiebroek'"), d.get_police_data("politiebureau", "politiebureaus", "'Ijsselmonde'"), d.get_police_data("politiebureau", "politiebureaus", "'Kralingen-Crooswijk'"), d.get_police_data("politiebureau", "politiebureaus", "'Noord'"), d.get_police_data("politiebureau", "politiebureaus", "'Overschie'"), d.get_police_data("politiebureau", "politiebureaus", "'Prins-Alexander'"), d.get_police_data("politiebureau", "politiebureaus", "'Centrum'"))
politiebureaus_std = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
rects2 = ax.bar(ind + width, politiebureaus, width, color='b', yerr=politiebureaus_std)

# add some text for labels, title and axes ticks
ax.set_ylabel('% criminaliteit/het aantal politiebureaus')
ax.set_title('Het gemiddelde percentage van criminaliteit en het aantal politiebureas per wijk (2009)')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('Charlois', 'Delfshaven', 'Feijenoord', 'Hillegersberg-Schiebroek', 'Ijsselmonde', 'Kralingen-Crooswijk', 'Noord', 'Overschie', 'Prins-Alexander', 'Centrum'))

ax.legend((rects1[0], rects2[0]), ('Percentage criminaliteit', 'Het aantal politiebureaus'))


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()


